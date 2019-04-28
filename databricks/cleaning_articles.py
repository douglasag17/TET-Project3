%python
from pyspark.sql.functions import regexp_replace, concat_ws
from pyspark.ml.feature import StopWordsRemover
from pyspark.ml.feature import Tokenizer, RegexTokenizer
import pyspark.sql.functions as f
from collections import defaultdict
# File location and type
file_path = "dbfs:///FileStore/tables/*.csv"
df = spark.read.csv(file_path, header="true", inferSchema="true").select("id", "title", "content")
df = df.filter(df.content.isNotNull())#Removing null values
df = df.filter(df.title.isNotNull())#Removing null values
df = df.withColumn('content', regexp_replace('content', '[^0-9a-zA-Z]+', ' '))#remove special characteres
df = df.withColumn('content', regexp_replace('content', '(?:^| )\w(?:$| )', ' '))#remove single words
#Removing stopwords
tokenizer = RegexTokenizer(inputCol="content", outputCol="words", pattern="\\W")
tokenized = tokenizer.transform(df).select('id', 'title' ,'words')
remover = StopWordsRemover(inputCol="words", outputCol="filtered")
cleanedDataFrame = remover.transform(tokenized).select('id', 'title' ,'filtered')
cleanedDataFrame = cleanedDataFrame.withColumn('filtered', concat_ws(' ', cleanedDataFrame.filtered))
frame = cleanedDataFrame.toPandas()
