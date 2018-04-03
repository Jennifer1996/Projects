#!/usr/bin/env python
# coding:utf8
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

# 加载包
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

# # 训练模型
# sentences = LineSentence('wiki.zh.word.text')
# model = Word2Vec(sentences, size=128, window=5, min_count=5, workers=4)
#
# # 保存模型
# model.save('word_embedding_128')

# 加载模型
model = Word2Vec.load("word_embedding_128")

# 使用模型
#items = model.most_similar(u'中国')
# for item in items:
#     print item[0],item[1]

print model.similarity(u'男人',  u'女人')
print model.similarity(u'人',  u'狗')
