dictionary = defaultdict(list)
for i, content in enumerate(frame['filtered']):
    article = str(frame['id'].iloc[i]) +","+ str(frame['title'].iloc[i])
    for word in str(content).split():
        if dictionary.get(word) == None:
            dictionary[word].append([1, article])
        else:
            if dictionary[word][-1][1] == article:
                dictionary[word][-1][0] += 1
            else:
                dictionary[word].append([1, article])

# Busqueda
word = "trump"
word = word.lower()
totalCount = 0
for i in range(len(dictionary[word])):
        totalCount += dictionary[word][i][0]
sortedList = sorted(dictionary[word], key = lambda k: k[0], reverse=True)
if len(sortedList) >= 10:
        for i in range(10):
                print(sortedList[i])
else:
        print(sortedList)
print(word + " is " + str(totalCount) + " times in all the news.")