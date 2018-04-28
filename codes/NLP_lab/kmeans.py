import pickle
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter

with open('/Users/chensi/Desktop/lab/embeddings.pkl','rb') as fin:
    embeddings=pickle.load(fin)

with open('/Users/chensi/Desktop/lab/vocab.pkl','rb') as fin:
    vocab=pickle.load(fin)

with open('/Users/chensi/Desktop/lab/word2id.pkl','rb')as fin:
    word2id=pickle.load(fin)


estimator = KMeans(n_clusters=500)#构造聚类器
estimator.fit(embeddings)#聚类
label_pred = estimator.labels_ #获取聚类标签
cln = []
for i in range(500):
    cln.append([])

for i, c in enumerate(label_pred):
    cln[c].append(i)

print(cln[0])

cw = []
for i in range(500):
    cw.append([])

for i, c in enumerate(cln):
    cw[i].extend([vocab[t] for t in c])

for i in range(30):
    print (cw[i])
#print(cw[0])
#print(cw[10])]

with open('/Users/chensi/Desktop/lab/kmeans.pkl','wb') as fout:
    pickle.dump(cw, fout)


