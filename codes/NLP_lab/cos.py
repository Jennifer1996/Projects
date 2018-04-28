import pickle
import numpy as np

with open('/Users/chensi/Desktop/lab/article.pkl','rb') as fin:
    article=pickle.load(fin)

print(article[0])
print(article[500])

vector1 = article[0]
vector2 = article[500]

op7=np.dot(vector1,vector2)/(np.linalg.norm(vector1)*(np.linalg.norm(vector2)))
print(op7)

'''
vector1=[]
vector2=[]
ops=[]
for i in range(len(article)):
    vector1.append(article[i])
    for j in range(len(article)):
        vector2.append(article[j])
        ops.append(np.dot(vector1[i],vector2[j])/(np.linalg.norm(vector1)*(np.linalg.norm(vector2))))

print(ops[0])

'''
    
