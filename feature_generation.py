import math
from numpy import *
from sklearn.feature_extraction.text import TfidfTransformer

def feature_extraction(source_file, feature_file):
    #get the 1st feature
    current_source_file = source_file
    word_diction = {}
    for line in open(current_source_file):
        words = line.split(",")
        for single_word in words:
            if single_word in word_diction:
                word_diction[single_word] += 1
            else:
                word_diction[single_word] = 0
    feature_one_unigram_vectors = []
    for line in open(current_source_file):
        tempwords_feature = []
        tempwords_dic = {}
        words = line.split(",")
        for single_word in words:               
            if single_word in tempwords_dic:
                tempwords_dic[single_word] += 1
            else:
                tempwords_dic[single_word] = 0
        for single_word in words:
            if single_word in word_diction:
                tempwords_feature.append(tempwords_dic[single_word])
            else:
                tempwords_feature.append(0)
        feature_one_unigram_vectors.append(array(tempwords_feature))
    feature_one_vectors_matrix = array(feature_one_unigram_vectors)
    transformer = TfidfTransformer(smooth_idf = False)
    tfidf = transformer.fit_transform(feature_one_vectors_matrix)
    feature_one_tfidf_array = tfidf.toarray()
    