# Tópicos Especiales en Telemática Proyecto 3: Bigdata, Spark

- Douglas Ardila Garcés dardila5@eafit.edu.co
- Andrés Felipe Avendaño aavenda1@eafit.edu.co
- Felipe Macías Herrera fmacias1@eafit.edu.co

## Ambiente de ejecución
El proyecto se debe ejecutar en un cluster de Databricks Community

## Preparación de datos
Se trabajó sobre el dataset [all-the-news](https://www.kaggle.com/snapcrack/all-the-news), el cual contiene 143000 noticias. 
Primero, se realizó la preparación de los datos a través del siguiente pre-procesamiento:
1. Se borraron todos los caracteres especiales (. , % ( ) ‘ “ ...., mediante la expresión regular: '[^0-9a-zA-Z]+'
2. Se borraron todas las stopwords haciendo uso de [StopWordsRemover](https://spark.apache.org/docs/2.2.0/ml-features.html#stopwordsremover) de Spark.
3. Se borraron todas las palabras de longitud 1 mediante la expresión regular: '(?:^| )\w(?:$| )'

## Búsqueda en índice invertido
Un índice invertido es un mecanismo orientado a palabras para indexación de documentos. El propósito de un índice invertido es permitir la rápida búsqueda en un texto completo, a un costo de procesamiento mayor cuando un documento se agrega a la base de datos.
El índice invertido tendrá la frecuencia de cada palabra en el titulo+descripción.
Donde por cada palabra que se ingrese por teclado en el Notebook, se liste en orden descendente por frecuencia de palabra en el contenido de la noticia, las noticias más relevantes.


## Agrupamiento de noticias

