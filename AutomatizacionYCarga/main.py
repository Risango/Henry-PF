import functions_framework
import logging
import os
import traceback
import re
from google.cloud import bigquery
from google.cloud import storage
import google.api_core.exceptions  # Importa el módulo google.api_core.exceptions
import yaml

with open("./schemas.yaml") as schema_file:
    config = yaml.load(schema_file, Loader=yaml.Loader)

PROJECT_ID = os.getenv('vocal-framework-427422-q6')
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

def _load_table_from_uri(bucket_name, file_name, tableSchema, tableName):
    uri = 'gs://%s/%s' % (bucket_name, file_name)
    table_id = BQ.dataset(BQ_DATASET).table(tableName)

    schema = create_schema_from_yaml(tableSchema)
    print(schema)
    job_config.schema = schema

    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    job_config.write_disposition = 'WRITE_APPEND'

    load_job = BQ.load_table_from_uri(
        uri,
        table_id,
        job_config=job_config,
    )

    try:
        load_job.result()  # Espera a que el trabajo de carga termine.
        print("Job finished.")
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
    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"Updated: {updated}")
    streaming(data)
