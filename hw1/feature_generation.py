import math
from numpy import *
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD

def feature1_unigram_extraction(source_file):
    #get the 1st feature
    vectorized = CountVectorizer()
    matrix = vectorized.fit_transform(open(source_file))
    return matrix
    
def feature2_unigram_tfidf_extraction(feature_one_vectors_matrix):
    
    transformer = TfidfTransformer(smooth_idf = False)
    tfidf = transformer.fit_transform(feature_one_vectors_matrix)
    feature_one_tfidf_array = tfidf
    
    return feature_one_tfidf_array
    
def feature3_normal_tfidf_extraction(source_file):
    feature_three_vectors_matrix = feature1_unigram_extraction(source_file)
    feature_three_tfidf_array = feature2_unigram_tfidf_extraction(feature_three_vectors_matrix)
    return feature_three_tfidf_array
    
def feature4_lsi_extraction(feature_three_tfidf_array):
    svd = TruncatedSVD(n_components=100)
    feature_four_lsi_array = svd.fit_transform(feature_three_tfidf_array)
    return feature_four_lsi_array




