# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:28:30 2016

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:02:58 2016

@author: user
"""
import scipy as sp
import numpy as np
from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import  TfidfVectorizer
import nltk

pro = 'Eclipse UI'

movie_reviews = load_files(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\%s\endata'%pro) 
target = []
data = [] 
for i in range(len(movie_reviews.data)):
    data += movie_reviews.data[i].split('\n')
for i in range(len(movie_reviews.data)):
    for j in range(len(movie_reviews.data[i].split('\n'))):
        target.append(movie_reviews.target[i])
#print target
test_time = 100
precise = []
for runtime in range(test_time):
    doc_terms_train, doc_terms_test, y_train, y_test\
        = train_test_split(data, target, test_size = 0.1)
    trainset = [[] for i in range(len(movie_reviews.data))]
    trainlabel = []
    for i in range(len(doc_terms_train)):
        trainset[y_train[i]].append(doc_terms_train[i])
        trainlabel.append(y_train[i])
    trainset_s = [[] for i in range(len(trainset))]
    for i in range(len(trainset)):
        trainset_s[i] = ''.join(trainset[i]) 
    #print doc_terms_train
   
    count_vec = TfidfVectorizer(binary = False, decode_error = 'ignore',\
                                stop_words = 'english')
    x_train = count_vec.fit_transform(trainset_s)
    #x_test  = count_vec.transform(doc_terms_test)
    #x       = count_vec.transform(movie_reviews.data)
    #y       = movie_reviews.target
    #res = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\%s\ti.txt'%pro, 'w')
    #res2 = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\tomcat\train.txt', 'w')
    #res3 = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\tomcat\test.txt', 'w')
    #for ele in doc_terms_train:
    #    res2.writelines(ele)
    #print(doc_terms_train)
    #for ele in doc_terms_test:
    #    res3.writelines(ele)
    result = x_train.toarray()
    #print x_test.toarray()
    #print result
    #for i in range(len(result[0])):
    #    res.writelines(count_vec.get_feature_names()[i])
    #    res.writelines(' ')
    #    res.writelines(str(result[0][i]))
    #    res.writelines(' ')
    #    res.writelines(str(result[1][i]))
    #    res.writelines(' ')
    #    res.writelines(str(result[2][i]))
    #    res.writelines('\n')
    #print y_test
    featurelist = count_vec.get_feature_names()
    for ele in featurelist:
        ele = str(ele).lower()
    featurelist[featurelist.index('bug')] = 0
    
    featurelist[featurelist.index('error')] = 0
    #featurelist[featurelist.index('')] = 0
    score = []
    tage = []
    for sen in doc_terms_test:
        token = nltk.word_tokenize(sen)
        sc = 0
        sc_n = 0
        tag = 0
        for i in range(len(movie_reviews.target)):
            for j in range(len(token)):
                try:
                    index = featurelist.index(token[j].lower())
                    #print featurelist[index], token[j], i, j
                    sc += result[i][index]
                except:
                    #print token[j]
                    sc += 0
            if sc > sc_n:
                sc_n = sc
                tag = i
            sc = 0
        score.append(sc_n)
        tage.append(tag) 
    isequal = 0
    for i in range(len(tage)):
        if tage[i] == y_test[i]:
            isequal += 1
    precise.append(float(isequal)/len(tage))
    r1 = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\tage_%s.txt'%runtime, 'w')
    r2 = open(r'D:\effort-awareness\Tomcat project\3sub\tf_idf\y_test_%s.txt'%runtime, 'w')
    for i in range(len(tage)):
       r1.writelines(str(tage[i]))
       r1.writelines('\n')
    r1.close()    
    for i in range(len(y_test)):
        r2.writelines(str(y_test[i]))
        r2.writelines('\n')
    r2.close()
print np.mean(precise)

    #print(count_vec.get_feature_names())
    #print result
    #print(x_train.toarray())
    #print(movie_reviews.target)
