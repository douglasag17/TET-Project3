grouping = defaultdict(dict)
for i, content in enumerate(frame['filtered']):
    id_ = str(frame['id'].iloc[i])
    words = {}
    for word in str(content).split():
      if word not in words:
          words[word] = 1
      else:
          words[word] += 1
    words = sorted(words.items(), key=lambda kv: kv[1], reverse = True)[:10]
    grouping[id_] = words
news = {}

# Busqueda
id_ = '17295'
title = cleanedDataFrame.filter(cleanedDataFrame.id == id_).collect()[0][1]
wordsN = grouping.get(id_)
dictOfWords = { i[0] : i[1] for i in wordsN }
for item in grouping.items():
    cont=0
    for word in item[1]:
        if word[0] in dictOfWords:
            cont += word[1]+dictOfWords[word[0]]
    news[item[0]]=cont
news = sorted(news.items(),key=lambda kv: kv[1], reverse = True)[:10]
ids_ = []
for i in news:
    ids_.append(i[0])
print(id_, title, ids_)
