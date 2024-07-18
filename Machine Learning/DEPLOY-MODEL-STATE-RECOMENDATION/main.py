import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
from sklearn.impute import SimpleImputer
import joblib

# Cargar el modelo logístico y el scaler
model = joblib.load('model.pkl')
app = Flask(__name__)

try:
    Business = pd.read_csv("Business.csv", sep=',', encoding='utf-8')  # DataFrame de negocios con varias columnas
    data = pd.read_csv("Business_ModeloRecomendacion.csv", sep=',', encoding='utf-8')
except pd.errors.ParserError as e:
    print(f"Error al leer el archivo CSV: {e}")

def recommend_states_for_business(business_id):
    # Filtrar datos para obtener las características relevantes para el business_id
    business_data = Business[Business['business_id'] == business_id][['stars', 'review_count', 'ingresos por negocio']]
    
    if business_data.empty:
        raise ValueError(f'No se encontraron datos para el business_id: {business_id}')
    
    # Verificar que todas las columnas necesarias están presentes
    if business_data.isnull().any().any():
        missing_columns = business_data.columns[business_data.isnull().any()].tolist()
        raise ValueError(f'Faltan valores en las columnas {missing_columns} para el business_id: {business_id}')
    
    # Imputar valores faltantes si los hay
    imputer = SimpleImputer(strategy='mean')
    X_business = imputer.fit_transform(business_data)
    
    if X_business.shape[1] != 3:
        raise ValueError(f'El número de características es incorrecto para el business_id: {business_id}')
    
    # Obtener el estado actual del negocio
    current_state = data[data['business_id'] == business_id]['state'].iloc[0]
    
    # Predecir probabilidades de estados usando el modelo
    predicted_probabilities = model.predict_proba(X_business.reshape(1, -1))
    
    # Obtener las etiquetas de clases del modelo
    classes = model.classes_
    
    # Ordenar las probabilidades y estados por probabilidad descendente, excluyendo el estado actual
    sorted_probabilities_indices = np.argsort(predicted_probabilities[0])[::-1]
    recommended_states = [classes[i] for i in sorted_probabilities_indices if classes[i] != current_state][:2]
    
    return recommended_states

@app.route('/', methods=['POST'])
def index():
    data = request.json
    business_id = data.get('business_id')
    if business_id is None:
        return jsonify({'error': 'No se proporcionó el business_id'}), 400

    try:
        resultado = recommend_states_for_business(business_id)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
    negocio_info = Business[Business['business_id'] == business_id].to_dict(orient='records')
    
    if negocio_info:
        negocio_info = negocio_info[0]  # Convertir de lista de diccionarios a un solo diccionario
    else:
        negocio_info = {}
    
    return jsonify({
        'estados_recomendados_para_el_negocio': resultado,
        'negocio_info': negocio_info
    })

if __name__ == '__main__':
    app.run(debug=True)
