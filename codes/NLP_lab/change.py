import pickle

with open('/Users/chensi/Desktop/lab/kmeans.pkl','rb') as fin:
    kmeans=pickle.load(fin)
with open('/Users/chensi/Desktop/lab/words.pkl','rb') as fin:
    words=pickle.load(fin)

dc = {}
for i, c in enumerate(kmeans):
    for w in c:
        dc[w] = i
res = []
for i in range(len(words)):
    tmp = []
    for j in range(len(words[i])):
        if words[i][j] in dc.keys():
            tmp.append(dc[words[i][j]])
    res.append(tmp)

print(res[10])
print(res[100])
with open('/Users/chensi/Desktop/lab/dc.pkl','wb') as fout:
    pickle.dump(dc,fout)

with open('/Users/chensi/Desktop/lab/res.pkl','wb') as fout:
    pickle.dump(res,fout)
