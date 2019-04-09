import pandas as pd
import glob
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords

stopWords = set(stopwords.words('english'))
columns = ['id', 'title', 'content']
allFiles = glob.glob("*.csv")
frame = pd.DataFrame()
i = 1
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0, usecols=columns)
    df['content'] = df['content'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stopWords)]))
    df['content'] = df['content'].str.lower()
    df['content'] = df['content'].str.replace(',', ' ')
    df['content'] = df['content'].str.replace('.', ' ')
    df['content'] = df['content'].str.replace(';', ' ')
    df['content'] = df['content'].str.replace(':', ' ')
    df['content'] = df['content'].str.replace('?', ' ')
    df['content'] = df['content'].str.replace('!', ' ')
    df['content'] = df['content'].str.replace('"', ' ')
    df['content'] = df['content'].str.replace('#', ' ')
    df['content'] = df['content'].str.replace('”', ' ')
    df['content'] = df['content'].str.replace('’', ' ')
    df['content'] = df['content'].str.replace('[', ' ')
    df['content'] = df['content'].str.replace(']', ' ')
    df['content'] = df['content'].str.replace('(', ' ')
    df['content'] = df['content'].str.replace(')', ' ')
    df['content'] = df['content'].str.replace('“', ' ')
    df['content'] = df['content'].str.replace('‘', ' ')
    df['content'] = df['content'].str.replace('\t', ' ')
    df.to_csv("Particles"+str(i)+".csv", sep=',', index=True, header=True)
    i+=1
