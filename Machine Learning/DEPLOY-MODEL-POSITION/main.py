import pandas as pd
from flask import Flask, request, jsonify
from scipy.sparse import hstack
import joblib
import json

# Cargar el modelo logístico y el scaler
modelo_logistico = joblib.load('modelo_logistico.pkl')
scaler = joblib.load('scaler.pkl')

app = Flask(__name__)

try:
    Business = pd.read_csv("Business_ModeloRecomendacion.csv", sep=',', encoding='utf-8')  # DataFrame de negocios con varias columnas
except pd.errors.ParserError as e:
    print(f"Error al leer el archivo CSV: {e}")

features = ['stars', 'review_count', 'state']
Business['exitoso'] = ((Business['stars'] > 3.0) & (Business['review_count'] > 50)).astype(int)
X = Business[features]
y = Business['exitoso']
X = pd.get_dummies(X, columns=['state'], drop_first=True)

def predecir_exito(stars, review_count, state):
    entrada = pd.DataFrame({
        'stars': [stars],
        'review_count': [review_count],
        'state': [state]
    })
    entrada = pd.get_dummies(entrada, columns=['state'], drop_first=True)
    
    for col in X.columns:
        if col not in entrada.columns:
            entrada[col] = 0
    
    # Reordenar las columnas para que coincidan con el modelo
    entrada = entrada[X.columns]
    
    # Escalar los datos de entrada
    entrada_scaled = scaler.transform(entrada)
    
    # Hacer la predicción
    prediccion = modelo_logistico.predict(entrada_scaled)
    
    # Devolver el resultado
    resultado = "Exitoso" if prediccion[0] == 1 else "Sin éxito"
    return {
        'resultado': resultado,
        'prediccion': int(prediccion[0])
    }

@app.route('/', methods=['POST'])
def index():
    data = request.json
    stars = data.get('stars')
    review_count = data.get('review_count')
    state = data.get('state')
    
    if stars is None or review_count is None or state is None:
        return jsonify({'error': 'Se requieren las variables stars, review_count y state'}), 400

    resultado = predecir_exito(stars, review_count, state)
    negocio_info = {'stars': stars, 'review_count':review_count, 'state':state}
    
    return jsonify({
        'resultado': resultado,
        'negocio_info': negocio_info
    })

if __name__ == '__main__':
    app.run(debug=True)
