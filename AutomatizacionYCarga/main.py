import functions_framework
import logging
import os
import traceback
import re
from google.cloud import bigquery
from google.cloud import storage
import google.api_core.exceptions  # Importa el módulo google.api_core.exceptions
import yaml
import json

with open("./schemas.yaml") as schema_file:
    config = yaml.load(schema_file, Loader=yaml.Loader)

PROJECT_ID = 'vocal-framework-427422-q6'

BQ_DATASET = 'Business_Reviews'
CS = storage.Client()
BQ = bigquery.Client()
job_config = bigquery.LoadJobConfig()

def streaming(data):
    bucketname = data['bucket']
    print("Bucket name:", bucketname)
    filename = data['name']
    print("File name:", filename)
    timeCreated = data['timeCreated']
    print("Time Created:", timeCreated)
    
    try:
        for table in config:
            tableName = table.get('name')
            print(f"Checking table: {tableName}")  # Registro de depuración
            # Ajustar el patrón para que sea más flexible
            pattern1 = re.escape(tableName.replace('_', '-'))
            pattern2 = re.escape(tableName)
            print(f"Patterns: {pattern1}, {pattern2}")  # Registro de depuración
            
            # Convertir los patrones a expresiones regulares
            pattern1 = re.compile(pattern1, re.IGNORECASE)
            pattern2 = re.compile(pattern2, re.IGNORECASE)
            
            # Comprobar coincidencia
            if pattern1.search(filename) or pattern2.search(filename):
                print(f"Match found for table: {tableName}")  # Registro de depuración
                tableSchema = table.get('schema')
                _check_if_table_exists(tableName, tableSchema)
                tableFormat = table.get('format')
                print(f"Table format: {tableFormat}")  # Registro de depuración
                if tableFormat == 'NEWLINE_DELIMITED_JSON':
                    _load_table_from_uri(data['bucket'], data['name'], tableSchema, tableName)
            else:
                print(f"No match for table: {tableName}")  # Registro de depuración
    except Exception:
        print('Error streaming file. Cause: %s' % (traceback.format_exc()))

def _check_if_table_exists(tableName, tableSchema):
    table_id = BQ.dataset(BQ_DATASET).table(tableName)
    try:
        BQ.get_table(table_id)
    except Exception:
        logging.warn('Creating table: %s' % (tableName))
        schema = create_schema_from_yaml(tableSchema)
        table = bigquery.Table(table_id, schema=schema)
        table = BQ.create_table(table)
        print("Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id))

def extract_id_from_json(json_data, schema):
    for field in schema:
        if field.mode == 'REQUIRED':
            field_name = field.name
            if field_name in json_data:
                return field_name, json_data[field_name]
    return None, None

def check_id_exists(tableName, id_field, id_value):
    query = f"SELECT COUNT(1) as count FROM `{PROJECT_ID}.{BQ_DATASET}.{tableName}` WHERE CAST({id_field} AS STRING) = @id_value"
    query_params = [
        bigquery.ScalarQueryParameter("id_value", "STRING", str(id_value))
    ]
    job_config = bigquery.QueryJobConfig(query_parameters=query_params)
    query_job = BQ.query(query, job_config=job_config)
    results = query_job.result()
    for row in results:
        if row.count > 0:
            return True
    return False

def _load_table_from_uri(bucket_name, file_name, tableSchema, tableName):
    uri = 'gs://%s/%s' % (bucket_name, file_name)
    table_id = BQ.dataset(BQ_DATASET).table(tableName)

    schema = create_schema_from_yaml(tableSchema)
    print(schema)
    
    # Descargar el archivo JSON desde el bucket
    bucket = CS.bucket(bucket_name)
    blob = bucket.blob(file_name)
    content = blob.download_as_text().splitlines()  # Dividir en líneas
    
    valid_lines = []
    for line in content:
        json_data = json.loads(line)  # Cargar cada línea como JSON
        # Extraer el ID del JSON
        id_field, id_value = extract_id_from_json(json_data, schema)
        
        if id_field and id_value:
            print(f"El ID de la tabla '{tableName}' es: {id_value}")
            # Verificar si el ID existe en la tabla
            if not check_id_exists(tableName, id_field, id_value):
                valid_lines.append(line)
            else:
                print(f"El ID {id_value} ya existe en la tabla {tableName}. Eliminando registro.")
        else:
            print("ID no encontrado en el JSON.")
            valid_lines.append(line)

    if not valid_lines:
        print("No hay datos válidos para cargar.")
        return
    
    # Guardar las líneas válidas en un archivo temporal
    temp_filename = f"/tmp/{file_name}"
    with open(temp_filename, 'w') as temp_file:
        temp_file.write("\n".join(valid_lines))
    
    job_config.schema = schema
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    job_config.write_disposition = 'WRITE_APPEND'

    # Subir el archivo temporal al bucket
    temp_blob = bucket.blob(f"temp/{file_name}")
    temp_blob.upload_from_filename(temp_filename)
    temp_uri = f'gs://{bucket_name}/temp/{file_name}'

    load_job = BQ.load_table_from_uri(
        temp_uri,
        table_id,
        job_config=job_config,
    )

    try:
        load_job.result()  # Espera a que el trabajo de carga termine.
        print("Job finished.")
        # Eliminar el archivo temporal del bucket después de la carga exitosa
        temp_blob.delete()
    except google.api_core.exceptions.BadRequest as e:
        print(f"Job failed with error: {e.errors}")  # Imprime los detalles del error.



def create_schema_from_yaml(table_schema):
    schema = []
    for column in table_schema:
        schemaField = bigquery.SchemaField(column['name'], column['type'], column['mode'])
        schema.append(schemaField)
        if column['type'] == 'RECORD':
            schemaField._fields = create_schema_from_yaml(column['fields'])
    return schema

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data
    event_id = cloud_event["id"]
    event_type = cloud_event["type"]
    bucket = data["bucket"]
    name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]
    print(f"PROJECT_ID: {PROJECT_ID}")
    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"Updated: {updated}")
    streaming(data)