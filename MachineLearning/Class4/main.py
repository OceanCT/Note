import jieba
with open('./data/test.txt','r',encoding='utf-8') as  novelFile:
    novel = novelFile.read()
# print(novel)
stopwords = [line.strip() for line in open('./data/stop.txt','r',encoding='utf-8').readlines()]
novelList = list(jieba.lcut(novel))
# print(novelList)
novelDict  = {}

# 统计出词频字典
for word in novelList:
    if word not in stopwords:
        if len(word) == 1:
            continue
        else:
            novelDict[word] = novelDict.get(word,0)+1