%python
from pyspark.sql.functions import regexp_replace, concat_ws
from pyspark.ml.feature import StopWordsRemover
from pyspark.ml.feature import Tokenizer, RegexTokenizer
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
# File location and type
file_path = "dbfs:///FileStore/tables/*.csv"
stopWords = set(stopwords.words('english'))
df = spark.read.csv(file_path, header="true", inferSchema="true").select("id", "title", "content")
df = df.withColumn('content', regexp_replace('content', '[^0-9a-zA-Z]+', ' '))#remove special characteres
df = df.withColumn('content', regexp_replace('content', '(?:^| )\w(?:$| )', ' '))#remove single words

tokenizer = Tokenizer(inputCol="content", outputCol="words")
tokenized = tokenizer.transform(df).select('id', 'title' ,'words')

remover = StopWordsRemover(inputCol="words", outputCol="filtered")
cleanedDataFrame = remover.transform(tokenized).select('id', 'title' ,'filtered')
cleanedDataFrame = cleanedDataFrame.withColumn('filtered', concat_ws(' ', cleanedDataFrame.filtered))
display(cleanedDataFrame)