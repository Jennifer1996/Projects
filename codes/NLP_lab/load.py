import nltk
import numpy as np
import pickle

words=[]
filename='/Users/chensi/Desktop/lab/wiki.en.text.50d.vector'
def loadWord2Vec(filename):
    vocab = []
    embd = []
    cnt = 0
    fr = open(filename,'r')
    line = fr.readline().strip()
    word_dim = int(line.split(' ')[1])    
    vocab.append("unk")
    embd.append([0]*word_dim)
    for line in fr :
        row = line.strip().split(' ')
        vocab.append(row[0])
        embd.append(row[1:])
    print("loaded word2vec")
    fr.close()
    return vocab,embd

vocab,embd = loadWord2Vec(filename)
vocab_size = len(vocab)
embedding_dim = len(embd)
embedding = np.asarray(embd)
words = [(vocab[i], embd[i]) for i in range(vocab_size)]

#with open('/Users/chensi/Desktop/lab/vec_deal.pkl','wb') as fout:
#    pickle.dump(words,fout)
print("Load sucessfully")


