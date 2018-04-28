import pickle

with open('/Users/chensi/Desktop/lab/vec_deal.pkl','rb') as fin:
    vec=pickle.load(fin)
print("loading vec successfully")
print("vec len: " + str(len(vec)))

vec1 = {}
for i in range(len(vec)):
    vec1[vec[i][0]] = vec[i][1]
print("converting vec to vec1 successfully")
print("vec1 len: " + str(len(vec1)))

with open('/Users/chensi/Desktop/lab/value_words.pkl','rb') as fin:
    words=pickle.load(fin)
print("loading words successfully")
print("words len: " + str(len(words)))

values=[]

for i in range(len(words)):
    if words[i] not in vec1: continue
    values.append((words[i], vec1[words[i]]))
print("values len: " + str(len(values)))

for value in values:
    print(value)

with open('/Users/chensi/Desktop/lab/values.pkl','wb') as fout:
    pickle.dump(values,fout)
print("loading values successfully")
