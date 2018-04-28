# coding:utf-8  
import nltk
import pickle
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.feature_extraction.text import TfidfTransformer  

#语料  
with open('/Users/chensi/Desktop/lab/res.pkl','rb') as fin:
    corpus=pickle.load(fin)

#print(corpus[0])
vec = []
for c in corpus:
    vec.append(' '.join([str(t) for t in c]))

#print (vec[2])
#print(vec[200])
#将文本中的词语转换为词频矩阵  
vectorizer = CountVectorizer()  
#计算个词语出现的次数  
X = vectorizer.fit_transform(vec)  
#获取词袋中所有文本关键词  
word = vectorizer.get_feature_names()  
#print (word)  
#查看词频结果  
#print (X.toarray())  
  
  
#类调用  
transformer = TfidfTransformer()  
#print (transformer)  
#将词频矩阵X统计成TF-IDF值  
tfidf = transformer.fit_transform(X)  
#查看数据结构 tfidf[i][j]表示i类文本中的tf-idf权重  
v = tfidf.toarray()

print("Article vectors is here:")
print(v[0])

#with open('/Users/chensi/Desktop/lab/article.pkl','wb') as fout:
#    pickle.dump(v,fout)


