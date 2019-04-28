# Tópicos Especiales en Telemática Proyecto 3: Bigdata, Spark

- Douglas Ardila Garcés dardila5@eafit.edu.co
- Andrés Felipe Avendaño aavenda1@eafit.edu.co
- Felipe Macías Herrera fmacias1@eafit.edu.co

## Ambiente de ejecución
El proyecto se debe ejecutar en un cluster de Databricks Community

## Preparación de datos

Se trabajó sobre el dataset [all-the-news](https://www.kaggle.com/snapcrack/all-the-news), el cual contiene 143000 noticias. Entonces primero preparamos los datos a traves a traves del siguiente pre-procesamiento:
1. Borramos todos los caracteres especiales (. , % ( ) ‘ “ ....
2. Borramos todas las stopwords
3. Borramos todas las palabras de longitud 1

## Busqueda en índice invertido
Un indice invertido es un mecanismo orientado a palabras para indexacion de documentos. El propósito de un índice invertido es permitir el rápido búsquedas de texto completo, a un costo de procesamiento mayor cuando un documento se agrega a la base de datos.
En el índice invertido tendrá la frecuencia de cada palabra en el titulo+descripción.
Donde por cada palabra que se ingrese por teclado en el Notebook, se liste en orden descendente por frecuencia de palabra en el contenido <titulo> de la noticia, las noticias más relevantes. Listar máx 5 <frec,news_id,title>.


## Agrupamiento de noticias

