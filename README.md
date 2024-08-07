![Demo 3-01](https://github.com/user-attachments/assets/80eecdb4-3340-48fc-a079-1bfb13fbc8d3)
 

</div>

La distribución de tareas se ha asignado meticulosamente para aprovechar las especialidades y habilidades de cada integrante, asegurando así una ejecución eficiente y efectiva de cada sprint. Ricardo Andres Santana Contreras, como Project Manager y Business Analyst, lidera la planificación y gestión del proyecto, asegurando que los objetivos del sprint se alineen con las necesidades del negocio y coordinando las actividades del equipo. Angel David Mariscal Soto y Carlos Andres Ibarra Bolaños, ambos Data Analysts y Data Engineers, se encargan del desarrollo y mantenimiento de la arquitectura de datos, además de implementar procesos de ETL y automatización necesarios para el manejo eficiente de los datos. Daniel Gomero Alegre, nuestro Machine Learning Engineer, lidera el desarrollo y afinamiento de los modelos de machine learning, asegurando su integración y funcionamiento óptimo en la producción. Por otro lado, Jorge Enrique Caicedo Riascos y Raul Rodrigo Penayo, ambos Business Intelligence Analysts y Data Analysts, son fundamentales en la creación de dashboards y reportes, proporcionando insights críticos a través del análisis avanzado de datos para informar decisiones estratégicas.

</div>

<details>
<summary><strong>Índice</strong></summary>

- [Situación Actual](#situación-actual)
- [Alcance](#alcance)
- [Contexto](#contexto)
  - [Objetivos del Proyecto](#Objetivos-del-Proyecto)
- [KPIs](#KPIs)
- [Solución Propuesta](#solucion-propuesta)
- [Propuesta de Trabajo](#propuesta-de-trabajo)
- [Metodología de Trabajo](#metodología-de-trabajo)
  - [Sprint 1](#sprint-1)
  - [Sprint 2: Desarrollo y Construcción](#sprint-2-desarrollo-y-construcción)
  - [Sprint 3: Implementación y Optimización](#sprint-3-implementación-y-optimización)
- [Gantt de Actividades](#gantt-de-actividades)
- [Data Engineering](#data-engineering)
  - [Análisis Exploratorio de Datos](#analisis-exploratorio-de-datos)
  - [Stack Tecnológico](#stack-tecnologico)
  - [Resumen de la Arquitectura](#resumen-de-la-arquitectura)
- [Diccionario de Datos](#diccionario-de-datos)
- [Diagrama Entidad Relación](#diagrama-entidad-relacion)
- [Pipeline Carga Incremental](#pipeline-carga-incremental)
- [Dashboard](#dashboard)
- [Modelo Machine Learning](#modelo-machine-learning)
- [Datasets y Fuentes Complementarias](#datasets-y-fuentes-complementarias)
- [Conclusiones](#conclusiones)
</details>




## Situación Actual
Como **Insightful Data Solutions**, somos una consultora de vanguardia especializada en transformar datos complejos en soluciones claras y accionables para una variedad de industrias. Nos dedicamos a proporcionar servicios de análisis avanzados, integración de datos y soluciones de inteligencia empresarial, apoyando a las empresas en la optimización de sus operaciones y estrategias de marketing mediante el uso eficaz de los datos.

Nuestra gama de productos incluye desde soluciones de almacenamiento de datos hasta plataformas de análisis predictivo y sistemas de recomendación personalizados. Nuestra experiencia abarca diversos sectores, incluyendo retail, turismo, y hospitalidad, donde aplicamos nuestra profunda comprensión de las necesidades de datos para impulsar la toma de decisiones basada en evidencias.

En el contexto actual, enfrentamos el desafío de mejorar la experiencia del cliente en el ámbito de retail. Dukin' ha observado una variabilidad significativa en las opiniones de los clientes sobre sus servicios, lo que ha impactado directamente en su rendimiento, percepción de marca y posicion en el mercado. Esta situación destaca la necesidad crítica de una estrategia refinada de ubicación y servicio basada en una comprensión más profunda de las preferencias y comportamientos de los usuarios del cliente.

**Proyecto en Desarrollo:**
Estamos desarrollando una solución personalizada para Dunkin', que involucra la creación de un sistema de análisis de reseñas en plataformas como Yelp y Google Maps. Esta solución está diseñada para identificar tendencias en la satisfacción del cliente y predecir áreas de crecimiento potencial o riesgo, permitiendo a nuestro cliente adaptar sus estrategias de marketing y expansión de manera más informada y efectiva. El producto final busca no solo mejorar la ubicación y la calidad de los nuevos establecimientos, sino también optimizar las campañas de marketing y aumentar la retención y satisfacción del cliente a través de recomendaciones personalizadas basadas en el análisis de grandes volúmenes de datos de reseñas.

Este proyecto representa una aplicación directa de nuestra capacidad para convertir los datos en estrategias de negocio profundas y acciones específicas, abordando una problemática existente con una solución innovadora y basada en datos.

## Alcance
El objetivo general de este proyecto es desarrollar una solución integral de análisis y recomendación basada en datos de reseñas de usuarios en plataformas como Yelp y Google Maps para la tienda de conveniencia Dunkin'. Esta solución permitirá identificar tendencias en la satisfacción del cliente, predecir áreas de crecimiento o declive potencial, y optimizar las estrategias de marketing y expansión de nuestros clientes en el sector de turismo y hospitalidad. Nuestro cliente nos ha contactado ya que busca incrementar su presencia el mercado de forma que logre superar a sus competidores.


## Contexto
La opinión de los usuarios es un dato muy valioso que crece día a día gracias a plataformas de reseñas. Su análisis puede ser determinante para la planificación de estrategias. Yelp es una plataforma de reseñas de todo tipo de negocios (restaurantes, hoteles, servicios, entre otros). Los usuarios utilizan el servicio y luego suben su reseña según la experiencia que han recibido. Esta información es muy valiosa para las empresas ya que les sirve para enterarse de la imagen que tienen los usuarios de los distintos locales, siendo útil para medir el desempeño y utilidad del local, además de saber en qué aspectos hay que mejorar el servicio.

Además, Google posee una plataforma de reseñas de todo tipo de negocios (restaurantes, hoteles, servicios, entre otros) integrada en su servicio de localización y mapas Google Maps. Los usuarios utilizan el servicio y luego suben su reseña según la experiencia vivida. Muchos usuarios leen las reseñas de los lugares a los que planean ir para tomar decisiones sobre dónde comprar, comer, dormir, reunirse, etc. Esta información es muy valiosa para las empresas ya que les sirve para enterarse de la imagen que tienen los usuarios de los distintos locales, siendo muy útil para medir el desempeño y utilidad del local, además de identificar los aspectos del servicio a mejorar.


## Objetivos del Proyecto
1. **Identificar ubicaciones ideales para apertura de tiendas de conveniencia:**
   - Determinar en qué localización geográfica y con qué características abrir nuevos locales para maximizar el éxito basado en la información de reseñas de usuarios.
2. **Medir el rendimiento de las estrategias de mercadotecnia:**
   - Realizar seguimiento y monitoreo del nivel de las calificaciones de los clientes para que con esta información Dunkin' pueda mejorar su estrategia de ventas.
3. **Predecir tendencias del mercado a nivel nacional:**
   - Utilizar análisis de reseñas para predecir cuáles estados tienen mayor probabilidad de crecimiento o declive en el futuro cercano.
4. **Crear un sistema de recomendación personalizado:**
   - Implementar un sistema de recomendación que sugiere a Dunkin' qué servicios muestran una calificación positiva en las experiencias y preferencias de los usuarios. Todo esto, para sugerir servicios que permitan a Dunkin' aumentar sus ventas.

## KPIs
![kpifinalwdwSAFD-01](https://github.com/user-attachments/assets/94f74e50-75d2-4355-9491-d8b63c8291fe)
### Identificar Ubicaciones Ideales para Apertura de Locales:
- **Índice de Calificaciones Positivas por Ubicación**:
  - **Criterio**: Número de reseñas con 4 o más estrellas / Número total de reseñas por ubicación
  - **Fórmula**: (Índice promedio actual - Índice promedio anterior) / Índice promedio anterior
  - **Datos**: `Rating` y `Review_Count`
  - **KPI Meta**: 1% o más de incremento año con año.
 
### Medir el Rendimiento De las Estrategias de Mercadotecnia:
- **Incremento en Calificaciones Promedio**:
  - **Fórmula**: (Calificación promedio actual - Calificación promedio anterior) / Calificación promedio anterior
  - **Datos**: `Rating` y `Review_Count`
  - **KPI Meta**: 1% o más de incremento año con año.

### Predecir Tendencias del Mercado a Nivel Nacional
- **Tasa de Crecimiento Anual de Reseñas en Categorías Clave**:
  - **Fórmula**: (Número de reseñas al final del año - Número de reseñas al inicio del año) / Número de reseñas al inicio del año
  - **Datos**: `Rating` y `Review_Count`
  - **Meta**: 10% o más de incremento año con año. 

    
# Solucion Propuesta:
<br>

## Propuesta de Trabajo
1. **Recopilar, depurar y disponibilizar la información:**
   - Creación de una base de datos (DataWarehouse) de diferentes fuentes, tanto provistas por Henry como incorporadas por nosotros, corriendo en local o alojada en proveedores en la nube. La base de datos depurada deberá contemplar por lo menos dos tipos diferentes de extracción de datos (e.g. datos estáticos, llamadas a una API, scrapping, entre otros).
2. **Reporte y análisis significativos de la(s) línea(s) de investigación escogidas:**
   - El análisis debe contemplar las relaciones entre variables y concluir si existe una relación entre estas y los posibles factores que causan dicha relación en la realidad.
3. **Entrenamiento y puesta en producción de un modelo de machine learning:**
   - El modelo debe resolver un problema y conectar globalmente con los objetivos propuestos que se planteen como proyecto.

## Metodología de Trabajo

<p align="center">
  <img src="https://github.com/Risango/Henry-PF/blob/main/imagenes/sprints.png?raw=true" alt="Scrum Framework" style="width:100%;">
</p>


La metodología empleada en este proyecto se basa en el marco de trabajo **Scrum**, una forma ágil y flexible de manejar proyectos de desarrollo de software. Scrum se centra en la entrega continua de valor a través de ciclos iterativos y incrementales conocidos como *Sprints*.

### Sprint 1:


- **Planificación del Sprint:** Definición de las historias de usuario y tareas necesarias para este sprint.
- **Configuración del entorno de trabajo:** Instalación y configuración de todas las herramientas y tecnologías necesarias.
- **Sprint Planning:** Establecimiento de objetivos y entrega de componentes específicos alineados con los objetivos del negocio.
- **Daily Scrum:** Reuniones diarias para evaluar el progreso y adaptar el backlog según sea necesario.
- **Revisión del Sprint:** Al final del sprint, se revisa el trabajo completado y se presentan los incrementos del producto.



### Sprint 2: Desarrollo y Construcción
- **Desarrollo de la arquitectura de datos**: Creación de modelos de datos eficientes y escalables.
- **Integración de fuentes de datos y ETL**: Automatización del procesamiento y consolidación de datos.
- **Daily Scrum**: Seguimiento diario para discutir avances y obstáculos.
- **Revisión y Retrospectiva del Sprint**: Evaluación del sprint para identificar mejoras y preparar el siguiente ciclo.

### Sprint 3: Implementación y Optimización
- **Afinamiento de modelos de machine learning**: Optimización de algoritmos y parámetros.
- **Implementación en producción**: Despliegue de modelos en el entorno de producción.
- **Documentación completa del proyecto**: Creación de documentos detallados y guías de usuario.
- **Daily Scrum**: Reuniones para asegurar que todos los miembros del equipo están alineados.
- **Revisión del Sprint y Retrospectiva**: Revisión final para asegurar la calidad y completitud del proyecto.

La colaboración interdisciplinaria entre los miembros del equipo es fundamental en Scrum, asegurando que cada aspecto del proyecto sea manejado por expertos en la materia, lo que optimiza los resultados y la eficiencia del desarrollo. Cada Sprint termina con una retrospectiva que permite al equipo reflexionar sobre sus procesos y buscar formas de mejorar en los siguientes ciclos.

## Productos a Entregar

### Modelo de Machine Learning
**Entrega**: Según el Gantt, el desarrollo inicial del modelo comienza en el Sprint 2 con pruebas de versiones, y se finaliza en el Sprint 3 con la implementación en producción.
- **Propósito**: Este modelo de ML está diseñado para analizar grandes volúmenes de datos y extraer patrones significativos que puedan mejorar la toma de decisiones y optimizar procesos internos. El modelo se afinará durante el Sprint 3 para asegurar su precisión y eficacia, permitiendo implementaciones prácticas en el entorno de producción.

### Reporte Dashboard
**Entrega**: El desarrollo del Dashboard se inicia en el Sprint 2 y se completa en el Sprint 3, con la presentación final de reportes y dashboards.
- **Función**: El Dashboard proporcionará una interfaz visual interactiva para mostrar los resultados analizados por el modelo de ML. Está diseñado para ser intuitivo, ofreciendo insights en tiempo real y facilitando el acceso a información clave para la toma de decisiones estratégicas. Los usuarios podrán visualizar métricas importantes, tendencias y alertas de manera eficiente.

Estos productos son esenciales para alcanzar los objetivos del proyecto y están alineados con las necesidades específicas del cliente, garantizando que cada entrega agregue valor significativo al negocio.


## Gantt de Actividades

<div align="center">
  <img src="https://github.com/Risango/Henry-PF/blob/main/imagenes/Gantt%20F.png?raw=true" alt="Gantt Chart 1" style="width: 800px;" />
</div>

# Data Engineering:

## Analisis Exploratorio de Datos:
<br>

![yelp-02](https://github.com/raulrodrigo567/Proyecto-1-2/assets/128632484/7a5e8361-1569-4751-9c51-205a66af6aa0)


![googlemaps-01](https://github.com/raulrodrigo567/Proyecto-1-2/assets/128632484/3d061fd4-d419-4b23-a39c-b6ee082499a3)

<div align="center">
  <img src="https://github.com/Risango/Henry-PF/blob/main/imagenes/Analisis%201.png?raw=true" alt="Analysis 1" style="width: 800px;" />
</div>

Una exploración más exhaustiva de los datos permitió llevar acabo un análisis de mercado donde se identifican los principales competidores de Dunkin’. Entres ellos se encuentran, Burger King, Taco Bell, McDonald’s y Starbucks. 

![Captura de pantalla 2024-07-19 010204](https://github.com/user-attachments/assets/45e2cdc5-caa0-4e73-a970-8a9e2c0fe141)

Además, se realizó un análisis FODA donde se identifican lo que son las Fortalezas, Oportunidades, Desventajas y Amenazas que posee Dunkin’.

## Stack Tecnologico

<div align="center">
  <img src="https://github.com/Risango/Henry-PF/blob/main/imagenes/Stack%20Tecnologico%20v3.png?raw=true" alt="Technological Stack" style="width: 800px;" />
</div>

## Resumen de la Arquitectura

### Sprint #1:
1. **Lenguajes y Frameworks**: 
   - Python (pyspark, pandas, numpy, matplotlib, seaborn)

### Sprint #2:
2. **Almacenamiento de Datos**: 
   - Google BigQuery, Google Cloud Storage
3. **Procesamiento y Transformación ETL**: 
   - Implementación de procesos de ETL (pandas, pyspark)
4. **Lenguajes y Frameworks**: 
   - Python (pyspark, pandas, numpy, matplotlib, seaborn)
5. **Diseño y Gestión de Bases de Datos**: 
   - MySQL Workbench, Cloud SQL
6. **Visualización de Datos**: 
   - Power BI

### Sprint #3:
7. **Procesamiento Distribuido**: 
   - Google Cloud Storage, Google BigQuery
8. **Orquestación de Pipelines**: 
   - Google Cloud Functions, Python
9. **Modelado de ML**: 
   - Scikit-learn, XGBoost
10. **Despliegue del Modelo de ML**: 
   - Google Cloud Run, Docker, Flask

## Ciclo de Vida del Dato & Justificación de la Arquitectura:

<div align="center">
  <img src="https://github.com/Risango/Henry-PF/blob/main/imagenes/ciclo%20de%20vida%20del%20datov2.png?raw=true" alt="Ciclo de Vida del Dato" width="1000">
</div>

#### 1. Almacenamiento de Datos
##### Google BigQuery
- **Definición**: Google BigQuery es un servicio de almacenamiento y análisis de datos de Google Cloud. Es un data warehouse totalmente administrado y altamente escalable.
- **Utilidad**: Permite ejecutar consultas SQL sobre grandes conjuntos de datos de manera rápida y escalable. Ideal para análisis de datos en tiempo real y procesamiento de grandes volúmenes de datos sin necesidad de gestionar la infraestructura subyacente.

#### 2. Procesamiento y Transformación ETL
##### Procesamiento ETL
- **Definición**: ETL (Extract, Transform, Load) es el proceso de extracción de datos de diversas fuentes, su transformación (limpieza, corrección de errores, normalización) y carga en un sistema de almacenamiento.
- **Utilidad**: Asegura que los datos estén limpios, precisos y en un formato adecuado para su análisis. Incluye eliminación de datos incompletos, corrección de errores, normalización de formatos, aplicación de reglas de negocio, agregaciones, cálculos derivados e integración de datos de diferentes fuentes.

#### 3. Procesamiento Distribuido
##### Google Cloud Storage
- **Definición**: Google Cloud Storage es un servicio de almacenamiento en la nube diseñado para almacenar grandes volúmenes de datos de manera segura y escalable.
- **Utilidad**: Permite el procesamiento rápido de grandes volúmenes de datos en paralelo, ideal para tareas de análisis y transformación a gran escala. Proporciona durabilidad, disponibilidad y acceso rápido a los datos almacenados.

#### 4. Orquestación de Pipelines
##### Google Cloud Functions
- **Definición**: Google Cloud Functions es un servicio de computación sin servidor que ejecuta funciones individuales en respuesta a eventos.
- **Utilidad**: Automatiza y orquesta los pipelines de datos, permitiendo la ejecución de funciones específicas basadas en eventos como la llegada de nuevos datos o disparadores programados. Ideal para la integración y automatización de procesos en tiempo real.

#### 5. Lenguajes y Frameworks
##### Python y sus Librerías
- **Python**: Un lenguaje de programación versátil y ampliamente utilizado en data science por su simplicidad y potencia.
  - **pyspark**: Integra Spark con Python para el procesamiento distribuido.
  - **pandas**: Facilita la manipulación y análisis de datos estructurados.
  - **numpy**: Proporciona soporte para grandes matrices y operaciones matemáticas.
  - **matplotlib y seaborn**: Librerías para la visualización de datos.

#### 6. Herramientas de Visualización
##### Power BI
- **Definición**: Power BI es una herramienta de análisis empresarial de Microsoft que permite crear visualizaciones interactivas y paneles de control.
- **Utilidad**: Permite a los usuarios explorar y analizar datos mediante gráficos interactivos, informes y dashboards, facilitando la toma de decisiones basadas en datos.

#### 7. Diseño de Modelos ER y Gestión de Bases de Datos
##### MySQL Workbench y Cloud SQL
- **MySQL Workbench**: Una herramienta visual para el diseño de bases de datos que facilita la modelación de datos y la administración de esquemas.
- **Cloud SQL**: Un servicio de bases de datos totalmente administrado para bases de datos MySQL en la nube de Google Cloud.
- **Utilidad**: Ayuda en la creación y gestión de bases de datos relacionales, asegurando la integridad y disponibilidad de los datos almacenados.

#### 8. Despliegue del Modelo de ML
##### Google Cloud Run y Flask
- **Google Cloud Run**: Un servicio completamente administrado para ejecutar contenedores en la nube de Google Cloud.
- **Flask**: Un microframework de Python para construir aplicaciones web y APIs.
- **Utilidad**: Facilita el despliegue de modelos de machine learning en producción de manera escalable y eficiente, permitiendo la exposición de funcionalidades a través de APIs web para su consumo externo.

## Diccionario de datos:

| Tabla            | Campo                   | Tipo de Dato | Descripción                                       | Ejemplo                                                |
|------------------|-------------------------|--------------|---------------------------------------------------|--------------------------------------------------------|
| Business         | Business_id             | String       | Es el id del negocio                              | --_lZuj_WCGnDG6n0emlRg                                 |
| Business         | Name                    | String       | El nombre del negocio                             | Ross Dress for Less                                    |
| Business         | Address                 | String       | El lugar del negocio                              | 700 Haddonfield Berlin Rd                              |
| Business         | Latitude                | Float        | Es la coordenada de la latitud                    | 39.8501                                                |
| Business         | Longitude               | Float        | Es la coordenada de la longitud                   | -74.98                                                 |
| Business         | Rating                  | Float        | Es la calificación promedio                       | 2.0                                                    |
| Business         | Review_Count            | Integer      | Es la cantidad de reviews                         | 13                                                     |
| Business         | State                   | String       | Es el estado resumido en dos caracteres           | PA                                                     |
| Categories       | Category_id             | Integer      | El id de la categoría                             | 2                                                      |
| Categories       | Category                | String       | La categoría                                      | Vintage & Consignment                                  |
| Business_Category| Business_Category_Id     | Integer      | El id de la tabla                                 | 4262                                                   |
| Business_Category| Business_id             | String       | El id del negocio                                 | ewMNH7OxjqKZUHvZN5JFiw                                 |
| Business_Category| Category_id             | Integer      | El id de la categoría que tiene el negocio        | 2                                                      |
| Users            | User_id                 | String       | Es el id del usuario                              | ---2PmXbF47D870stH1jqA                                 |
| Users            | Name                    | String       | Es nombre del usuario                             | Susan                                                  |
| Reviews          | Review_id               | String       | Es el id de la critica                            | --2CDvzn64m9BAhe4JnKCg                                 |
| Reviews          | Business_id             | String       | Es el id del negocio                              | jDOTVhWXkmLcsfM2KGd5Qg                                 |
| Reviews          | User_id                 | String       | Es el id del usuario que escribió la critica      | Xw7ZjaGfr0WNVt6s_5KZfA                                  |
| Reviews          | Rating                  | Float        | Es la calificación que marcó el usuario del negocio| 2.0                                                    |
| Reviews          | Text                    | String       | Es el texto de la critica                         | No. Just...no. Heat. Crowds of pretentious people. I just can't do it. |
| Reviews          | Date                    | Date         | Es la fecha en la que se escribió la critica      | 2013-08-04                                             |
| Tips             | Tip_id                  | Integer      | Es el id de la crítica o 'tip'                    | 6                                                      |
| Tips             | Business_id             | String       | Es el id del negocio                              | jDOTVhWXkmLcsfM2KGd5Qg                                 |
| Tips             | User_id                 | String       | Es el id del usuario que escribió la crítica o 'tip'| Xw7ZjaGfr0WNVt6s_5KZfA                                 |
| Tips             | Text                    | String       | Es el texto de la critica                         | No. Just...no. Heat. Crowds of pretentious people. I just can't do it. |
| Tips             | Date                    | Date         | Es la fecha en la que se escribió la critica      | 2013-08-04                                             |
| Tips             | Compliment_count        | Integer      | Es la cantidad de votos útiles hacia el 'tip'     | 1                                                      |

## Diagrama Entidad Relacion

<div align="center">
  <img src="https://github.com/Risango/Henry-PF/blob/main/imagenes/Diagrama%20Entidad.png?raw=true" alt="Diagrama Entidad" width="600">
</div>

### Diccionario de Datos y Estructura

El diccionario de datos detalla información clave extraída de Yelp y Google Maps:

- **Yelp:** Nombre del negocio, dirección, categorías, calificaciones, estado operativo
- **Google Maps:** Localización, atributos del comercio, medidas de seguridad

### Tablas Principales

- **Business:** `name`, `address`, `latitude`, `longitude`
- **Reviews:** `text`, `rating`, `date`, enlazando usuario y negocio

### Integración de Datos

La integración de Yelp y Google Maps enriquece nuestra base de datos, proporcionando una visión completa del comportamiento del consumidor y tendencias del mercado, crucial para decisiones estratégicas.

### Diagrama de Entidad Relación

Nuestro modelo de datos incluye las siguientes tablas clave interconectadas:

- **Business**
- **Reviews**
- **Users**
- **Categories**
- **Tips**

### Claves

- **Primary Keys:** Garantizan unicidad, ej. `Business_id` en Business
- **Foreign Keys:** Relacionan tablas, ej. `User_id` y `Business_id` en Reviews

### Aplicaciones y Ventajas

La integración de datos permite comprender mejor a clientes y competencia, identificar oportunidades y optimizar marketing. Analizar tendencias desde una base unificada es esencial para la competitividad y éxito empresarial.

## Pipeline Carga Incremental

<div align="center">
  <img src="https://github.com/Risango/Henry-PF/blob/main/imagenes/Pipeline%20Carga%20Incremental.png?raw=true" alt="Pipeline Carga Incremental" width="1000">
</div>

<div align="center">
  <h3 style="text-decoration: underline; text-transform: uppercase;">VIDEO EXPLICATIVO PIPELINE</h3>
  <a href="https://www.youtube.com/watch?v=K7m9_3nErjY">
    <img src="https://img.youtube.com/vi/6hyfh6FPalA/0.jpg" alt="Watch the video" style="width: 600px;" />
  </a>
</div>

## Dashboard

<div align="center">
  <a href="https://drive.google.com/drive/folders/1_mGYZEdVB_f2GSvkqIiknsexiLbvJPPM?hl=es" style="font-size:60px; text-decoration:none;">Link Archivo Dashboard</a>
</div>
<br>

![Captura de pantalla 2024-07-19 004745](https://github.com/user-attachments/assets/b5eb9fb0-2cdd-4f12-8094-b5f7231e8e6a)
![Captura de pantalla 2024-07-19 004832](https://github.com/user-attachments/assets/3d6fec51-a93e-418d-b1d0-752d3419f77d)



</div>

## Modelo Machine Learning
![Demo 2 (1)-01](https://github.com/user-attachments/assets/6324e0ab-da0e-4219-8642-bcdb490daf62)

</div>

Este proyecto de Machine Learning está diseñado para analizar datos en tres áreas clave: ubicaciones potenciales para Dunkin', preferencias de los usuarios, y estados con mayor crecimiento o declive. Utilizando diversos conjuntos de datos como ratings, estados, latitud, longitud, año, reseñas, usuarios y negocios, generamos salidas específicas que ayudan a tomar decisiones informadas. Para Dunkin', identificamos posibles nuevas ubicaciones mediante la latitud y longitud. Analizamos las preferencias de los usuarios para entender mejor sus necesidades y mejorar el servicio, y finalmente, evaluamos el crecimiento o declive de los estados para ajustar nuestras estrategias de mercado. Este enfoque integral nos permite optimizar operaciones y maximizar el impacto en el mercado.

# Conclusiones

<img src="https://github.com/Risango/Henry-PF/blob/main/imagenes/Conclusion%201.png?raw=true" alt="Descripción de la imagen 1" width="1000"/>
<img src="https://github.com/Risango/Henry-PF/blob/main/imagenes/conclusion%202.png?raw=true" alt="Descripción de la imagen 2" width="1000"/>

## Datasets y Fuentes Complementarias
- **Dataset de Google Maps:** Información sobre la ubicación de los comercios, su categoría, puntajes promedios, si están abiertos o no, sobre los usuarios, las reseñas que hicieron, cuántas reseñas hicieron, cuántos votos han recibido esas reseñas, entre otros.
- **Dataset de Yelp:** Información similar a la de Google Maps, con detalles adicionales sobre atributos del negocio, categorías, horarios, entre otros.
