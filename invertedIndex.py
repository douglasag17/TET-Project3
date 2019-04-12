from collections import defaultdict
import pandas as pd
import glob

columns = ['id', 'title', 'content']
allFiles = glob.glob("articles2.csv")
frame = pd.DataFrame()
list_ = []
dictionary = defaultdict(list)
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0, usecols=columns)
    list_.append(df)
frame = pd.concat(list_)
for i,content in enumerate(frame['content']):
    article = str(frame['id'].iloc[i]) +","+ str(frame['title'].iloc[i])
    for word in str(content).split():
        if dictionary.get(word) == None:
            dictionary[word].append([1, article])
        else:
            if dictionary[word][-1][1] == article:
                dictionary[word][-1][0] += 1
            else:
                dictionary[word].append([1, article])
while(True):
        word = input("Type the word: \quit:\n")
        if word == "\quit":
                break
        else:
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
                
