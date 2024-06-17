# Proyecto Final: Yelp & Google Maps - Reseñas y Recomendaciones

<div align="center">
  <img src="https://raw.githubusercontent.com/Risango/Henry-PF/main/DALL%C2%B7E%202024-06-16%2018.31.54%20-%20A%20professional%20and%20modern%20logo%20for%20a%20data%20consultancy%20company%20named%20'Insightful%20Data%20Solutions'.%20The%20logo%20should%20feature%20a%20sleek%20and%20minimalist%20design.webp" alt="Insightful Data Solutions Logo" width="250"/>
</div>


## Situación Actual
Como **Insightful Data Solutions**, somos una consultora de vanguardia especializada en transformar datos complejos en soluciones claras y accionables para una variedad de industrias. Nos dedicamos a proporcionar servicios de análisis avanzados, integración de datos y soluciones de inteligencia empresarial, apoyando a las empresas en la optimización de sus operaciones y estrategias de marketing mediante el uso eficaz de los datos.

Nuestra gama de productos incluye desde soluciones de almacenamiento de datos hasta plataformas de análisis predictivo y sistemas de recomendación personalizados. Nuestra experiencia abarca diversos sectores, incluyendo retail, turismo, y hospitalidad, donde aplicamos nuestra profunda comprensión de las necesidades de datos para impulsar la toma de decisiones basada en evidencias.

En el contexto actual, enfrentamos el desafío de mejorar la experiencia del cliente en el ámbito del turismo y la hospitalidad. Un conglomerado de empresas en este sector ha observado una variabilidad significativa en las opiniones de los clientes sobre sus servicios, lo que ha impactado directamente en su rendimiento y percepción de marca. Esta situación destaca la necesidad crítica de una estrategia refinada de ubicación y servicio basada en una comprensión más profunda de las preferencias y comportamientos del cliente.

**Proyecto en Desarrollo:**
Estamos desarrollando una solución personalizada para este conglomerado, que involucra la creación de un sistema de análisis de reseñas en plataformas como Yelp y Google Maps. Esta solución está diseñada para identificar tendencias en la satisfacción del cliente y predecir áreas de crecimiento potencial o riesgo, permitiendo a nuestro cliente adaptar sus estrategias de marketing y expansión de manera más informada y efectiva. El producto final busca no solo mejorar la ubicación y la calidad de los nuevos establecimientos, sino también optimizar las campañas de marketing y aumentar la retención y satisfacción del cliente a través de recomendaciones personalizadas basadas en el análisis de grandes volúmenes de datos de reseñas.

Este proyecto representa una aplicación directa de nuestra capacidad para convertir los datos en estrategias de negocio profundas y acciones específicas, abordando una problemática existente con una solución innovadora y basada en datos.

## Alcance
El objetivo general de este proyecto es desarrollar una solución integral de análisis y recomendación basada en datos de reseñas de usuarios en plataformas como Yelp y Google Maps. Esta solución permitirá identificar tendencias en la satisfacción del cliente, predecir áreas de crecimiento o declive potencial, y optimizar las estrategias de marketing y expansión de nuestros clientes en el sector de turismo y hospitalidad. El producto final incluirá un sistema de recomendación personalizado que ayudará a los usuarios a descubrir nuevas experiencias basadas en sus preferencias y experiencias previas.

## Contexto
La opinión de los usuarios es un dato muy valioso que crece día a día gracias a plataformas de reseñas. Su análisis puede ser determinante para la planificación de estrategias. Yelp es una plataforma de reseñas de todo tipo de negocios (restaurantes, hoteles, servicios, entre otros). Los usuarios utilizan el servicio y luego suben su reseña según la experiencia que han recibido. Esta información es muy valiosa para las empresas ya que les sirve para enterarse de la imagen que tienen los usuarios de los distintos locales, siendo útil para medir el desempeño y utilidad del local, además de saber en qué aspectos hay que mejorar el servicio.

Además, Google posee una plataforma de reseñas de todo tipo de negocios (restaurantes, hoteles, servicios, entre otros) integrada en su servicio de localización y mapas Google Maps. Los usuarios utilizan el servicio y luego suben su reseña según la experiencia vivida. Muchos usuarios leen las reseñas de los lugares a los que planean ir para tomar decisiones sobre dónde comprar, comer, dormir, reunirse, etc. Esta información es muy valiosa para las empresas ya que les sirve para enterarse de la imagen que tienen los usuarios de los distintos locales, siendo muy útil para medir el desempeño y utilidad del local, además de identificar los aspectos del servicio a mejorar.

## Rol a Desarrollar
Como parte de una consultora de datos, nos han contratado para poder realizar un análisis del mercado estadounidense. Nuestro cliente es parte de un conglomerado de empresas de restaurantes y afines y desean tener un análisis detallado de la opinión de los usuarios en Yelp y cruzarlos con los de Google Maps sobre hoteles, restaurantes y otros negocios afines al turismo y ocio, utilizando análisis de sentimientos para predecir cuáles serán los rubros de los negocios que más crecerán (o decaerán). Además, desean saber dónde es conveniente emplazar los nuevos locales de restaurantes y afines y desean poder tener un sistema de recomendación de restaurantes para los usuarios de ambas plataformas para darle al usuario, por ejemplo, la posibilidad de poder conocer nuevos sabores basados en sus experiencias previas.

## Propuesta de Trabajo
1. **Recopilar, depurar y disponibilizar la información:**
   - Creación de una base de datos (DataWarehouse) de diferentes fuentes, tanto provistas por Henry como incorporadas por nosotros, corriendo en local o alojada en proveedores en la nube. La base de datos depurada deberá contemplar por lo menos dos tipos diferentes de extracción de datos (e.g. datos estáticos, llamadas a una API, scrapping, entre otros).
2. **Reporte y análisis significativos de la(s) línea(s) de investigación escogidas:**
   - El análisis debe contemplar las relaciones entre variables y concluir si existe una relación entre estas y los posibles factores que causan dicha relación en la realidad.
3. **Entrenamiento y puesta en producción de un modelo de machine learning:**
   - El modelo debe resolver un problema y conectar globalmente con los objetivos propuestos que se planteen como proyecto.

## Datasets y Fuentes Complementarias
- **Dataset de Google Maps:** Información sobre la ubicación de los comercios, su categoría, puntajes promedios, si están abiertos o no, sobre los usuarios, las reseñas que hicieron, cuántas reseñas hicieron, cuántos votos han recibido esas reseñas, entre otros.
- **Dataset de Yelp:** Información similar a la de Google Maps, con detalles adicionales sobre atributos del negocio, categorías, horarios, entre otros.

## Objetivos del Proyecto
1. **Identificar la mejor ubicación y tipo de negocio:**
   - Determinar en qué localización geográfica y con qué características abrir nuevos locales para maximizar el éxito basado en las reseñas.
2. **Mejorar la estrategia de marketing:**
   - Mejorar las ventas y suministrar ideas para incrementar las ventas basadas en las reseñas de los usuarios.
3. **Predecir tendencias del mercado:**
   - Utilizar análisis de reseñas para predecir cuáles rubros de negocios tienen mayor probabilidad de crecimiento o declive en el futuro cercano.
4. **Crear un sistema de recomendación personalizado:**
   - Implementar un sistema de recomendación que sugiera restaurantes y otros negocios basados en las experiencias y preferencias de los usuarios.

## KPIs Propuestos
- **Para identificar la mejor ubicación y tipo de negocio:**
  - **Número de reseñas positivas por ubicación:** Meta: Identificar al menos 10 ubicaciones con más del 75% de reseñas positivas.
  - **Promedio de calificaciones por categoría de negocio:** Meta: Seleccionar categorías con un promedio de al menos 4.0 estrellas en las principales ubicaciones identificadas.
  - **Frecuencia de reseñas en nuevos locales sugeridos:** Meta: Lograr que los nuevos locales reciban al menos 100 reseñas en los primeros 6 meses de operación.
- **Para mejorar la estrategia de marketing:**
  - **Incremento en la calificación promedio después de campañas de marketing:** Meta: Aumentar la calificación promedio en al menos 0.5 estrellas tras las campañas de marketing.
  - **Número de reseñas que mencionan promociones:** Meta: Incrementar en un 20% las menciones de promociones en las reseñas durante las campañas de marketing.
  - **Aumento en el tráfico de clientes (medido por check-ins):** Meta: Aumentar los check-ins en al menos un 30% tras las campañas de marketing.
- **Para predecir tendencias del mercado:**
  - **Tendencia de calificaciones por categoría de negocio:** Meta: Identificar al menos 5 categorías con una tendencia creciente de 0.2 estrellas por año.
  - **Frecuencia de palabras clave positivas/negativas en reseñas:** Meta: Determinar que las categorías con mayor frecuencia de palabras clave positivas muestren un incremento del 10% anual en calificaciones.
  - **Predicción de crecimiento en número de reseñas:** Meta: Prever un crecimiento del 15% anual en el número de reseñas para las categorías de negocio con mayor tendencia positiva.

## Integrantes y Roles

<div align="center">

| Nombre                               | Siglas | Rol                                       |
|--------------------------------------|--------|-------------------------------------------|
| Angel David Mariscal Soto            | AD     | Data Analyst (DA), Data Engineer (DE)     |
| Ricardo Andres Santana Contreras     | RS     | Project Manager (PM), Business Analyst (BA)|
| Daniel Gomero Alegre                 | DG     | Machine Learning Engineer (MLE)           |
| Carlos Andres Ibarra Bolaños         | CA     | Data Analyst (DA), Data Engineer (DE)     |
| Jorge Enrique Caicedo Riascos        | JE     | Business Intelligence Analyst (BIA), Data Analyst (DA)|
| Raul Rodrigo Penayo                  | RR     | Business Intelligence Analyst (BIA), Data Analyst (DA)|

</div>

## Gantt de Actividades

<div align="center">
  <img src="https://github.com/Risango/Henry-PF/blob/main/Gantt.png?raw=true" alt="Gantt Chart" width="1000">
</div>

## Metodología de Trabajo
La metodología empleada en este proyecto se basa en prácticas ágiles y ciclos iterativos de desarrollo. Cada sprint se enfoca en la entrega de componentes específicos del proyecto, permitiendo revisiones constantes y adaptaciones según sea necesario. Esto asegura que el proyecto se mantenga alineado con los objetivos del negocio y responda de manera flexible a cualquier cambio en los requisitos o prioridades del cliente.

- **Sprint 1** se centra en la planificación, definición de alcance y preparación del entorno de trabajo, incluyendo la configuración de herramientas y tecnologías necesarias.
- **Sprint 2** aborda el desarrollo de la arquitectura de datos, la integración de fuentes de datos y la automatización de procesos de ETL, además de la preparación inicial de reportes y dashboards.
- **Sprint 3** se dedica al afinamiento de modelos de machine learning, implementación en producción y documentación completa del proyecto.

La colaboración interdisciplinaria entre los miembros del equipo garantiza que cada aspecto del proyecto sea manejado por expertos en la materia, optimizando los resultados y la eficiencia del desarrollo.
