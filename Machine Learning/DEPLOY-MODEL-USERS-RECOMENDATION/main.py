import pickle
import pandas as pd
import numpy as np
import re
from flask import Flask, request, jsonify
from scipy.sparse import hstack

# Cargar el modelo XGBoost
with open('modelo_xgb.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Cargar el transformador de target
with open('target_encoder.pkl', 'rb') as f:
    target_encoder = pickle.load(f)

# Cargar el vectorizador
with open('vect.pkl', 'rb') as f:
    vect = pickle.load(f)

app = Flask(__name__)

def limpiar_texto(texto):
    texto_limpio = re.sub(r'[^a-zA-Z0-9 ]', '', texto)
    texto_limpio = texto_limpio.lower()
    return texto_limpio


try:
    Reviews = pd.read_csv("Reviews_Recomendacion.csv", sep=',', encoding='utf-8') #Se necesita tener el archivo de Reviews_Recomendacion
except pd.errors.ParserError as e:
    print(f"Error al leer el archivo CSV: {e}")

# Función para recomendar usuarios
def recomendar_usuarios(business_id):
    df_filtrado = Reviews[Reviews['Business_id'] == business_id]
    
    df_filtrado['business_id_encoded'] = target_encoder.transform(df_filtrado['Business_id'])
    df_vect_text = vect.transform(df_filtrado['texto_final'])
    df_vect = hstack((df_vect_text, np.array(df_filtrado['business_id_encoded']).reshape(-1, 1)))
    
    probas = modelo.predict_proba(df_vect)
    df_filtrado['probabilidad'] = probas[:, 1]
    
    top_5_usuarios = df_filtrado.nlargest(5, 'probabilidad')[['User_id', 'probabilidad']]
    return top_5_usuarios['User_id'].tolist()

@app.route('/', methods=['POST'])
def index():
    business_id = request.json.get('business_id')
    if business_id is None:
        return jsonify({'error': 'No se proporcionó el business_id'}), 400

    usuarios_recomendados = recomendar_usuarios(business_id)
    return jsonify({'usuarios_recomendados': usuarios_recomendados})

if __name__ == '__main__':
    app.run(debug=True)
