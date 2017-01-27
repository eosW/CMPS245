#from preprocess import pre_processing
import csv

from feature_generation import feature1_unigram_extraction
from feature_generation import feature2_unigram_tfidf_extraction
from feature_generation import feature3_normal_tfidf_extraction
from feature_generation import feature4_lsi_extraction
from clustering import kmeans_clustering

tag_nonormal = "no_normal"
tag_normal = "normal"

def cmu_twitter_tagger_2_real_data_format():
    f_write_file = open("final_real_clinton_tokens_normal_taggered.csv", "w")
    line_num = 0
    for line in open("real_clinton_tokens_normal_taggered.csv"):
        line_num += 1
        if line_num % 500 == 0:
            print line_num   
        temp_string = line.split("\t")
        temp_real_word_ini = temp_string[0]
        temp_real_word = temp_real_word_ini.split(" ")
        temp_real_pos_ini = temp_string[1]
        temp_real_pos = temp_real_pos_ini.split(" ")
        
        temp_len = 0

        temp_sentence = ""
        temp_sentence_len = len(temp_real_word)
        for temp_single_word in temp_real_word:
            temp_len += 1
            if temp_real_pos[temp_len - 1] == "^" or temp_real_pos[temp_len - 1] == "Z":
                if temp_len == temp_sentence_len:
                    temp_sentence = temp_sentence[0:len(temp_sentence) - 1] + "\n"
            else:
                if temp_len == temp_sentence_len:
                    temp_sentence += temp_single_word + "\n"
                else:
                    temp_sentence += temp_single_word + " "

        f_write_file.write(temp_sentence.encode('utf-8'))

def nltk_format_2_cmu_twitter_pos_tagger_format():
    #generate real clinton tokens normal
    f_write_file = open("final_real_clinton_tokens_nonormal.csv", "w")
    line_num = 0
    for line in open("clinton_tokens_nonormal.csv"):
        line_num += 1
        if line_num % 500 == 0:
            print line_num
        temp_string = line.replace(",", " ")
        f_write_file.write(temp_string.encode('utf-8'))
 
#nltk_format_2_cmu_twitter_pos_tagger_format()       
#cmu_twitter_tagger_2_real_data_format()
    
#pre_processing("trump-50k.csv","trump_tokens_normal.csv", tag_nonormal)
#pre_processing("clinton-50k.csv","clinton_tokens_normal.csv", tag_nonormal)
data_no_normal_trump = "final_real_trump_tokens_nonormal.csv"
data_no_normal_clinton = "final_real_clinton_tokens_nonormal.csv"
data_normal_trump = "final_real_trump_tokens_normal_taggered.csv"
data_normal_clinton = "final_real_clinton_tokens_normal_taggered.csv"
unigram_feature1_array_trump, vocabulary_unigram_trump = feature1_unigram_extraction(data_no_normal_trump)
unigram_feature1_array_clinton, vocabulary_unigram_clinton = feature1_unigram_extraction(data_no_normal_clinton)
unigramtfidf_feature2_array_trump = feature2_unigram_tfidf_extraction(unigram_feature1_array_trump)
unigramtfidf_feature2_array_clinton = feature2_unigram_tfidf_extraction(unigram_feature1_array_clinton)
normaltfidf_feature3_array_trump, vocabulary_normal_trump = feature3_normal_tfidf_extraction(data_normal_trump)
normaltfidf_feature3_array_clinton, vocabulary_normal_clinton = feature3_normal_tfidf_extraction(data_normal_clinton)
lsi_feature4_array_trump = feature4_lsi_extraction(normaltfidf_feature3_array_trump)
lsi_feature4_array_clinton = feature4_lsi_extraction(normaltfidf_feature3_array_clinton)

unigram_feature1_array_trump_predict_result = kmeans_clustering(unigram_feature1_array_trump)
print len(unigram_feature1_array_trump_predict_result)

unigram_feature1_array_clinton_predict_result = kmeans_clustering(unigram_feature1_array_clinton)
print len(unigram_feature1_array_clinton_predict_result)

unigramtfidf_feature2_array_trump_predict_result = kmeans_clustering(unigramtfidf_feature2_array_trump)
print len(unigramtfidf_feature2_array_trump_predict_result)

unigramtfidf_feature2_array_clinton_predict_result = kmeans_clustering(unigramtfidf_feature2_array_clinton)
print len(unigramtfidf_feature2_array_clinton_predict_result)

normaltfidf_feature3_array_trump_predict_result = kmeans_clustering(normaltfidf_feature3_array_trump)
print len(normaltfidf_feature3_array_trump_predict_result)

normaltfidf_feature3_array_clinton_predict_result = kmeans_clustering(normaltfidf_feature3_array_clinton)
print len(normaltfidf_feature3_array_clinton_predict_result)

lsi_feature4_array_trump_predict_result = kmeans_clustering(lsi_feature4_array_trump)
print len(lsi_feature4_array_trump_predict_result)

lsi_feature4_array_clinton_predict_result = kmeans_clustering(lsi_feature4_array_clinton)
print len(lsi_feature4_array_clinton_predict_result)

id = range(50000)
stat_f1_trump = (' '.join('%s:%s' % (key, value) for (key, value) in zip(vocabulary_unigram_trump, unigram_feature1_array_trump[n, :].toarray().reshape(len(vocabulary_unigram_trump))) if value>0) for n in range(50000))
stat_f2_trump = (' '.join('%s:%s' % (key, value) for (key, value) in zip(vocabulary_unigram_trump, unigramtfidf_feature2_array_trump[n, :].toarray().reshape(len(vocabulary_unigram_trump))) if value>0) for n in range(50000))
stat_f3_trump = (' '.join('%s:%s' % (key, value) for (key, value) in zip(vocabulary_normal_trump, normaltfidf_feature3_array_trump[n, :].toarray().reshape(len(vocabulary_unigram_trump))) if value>0) for n in range(50000))
stat_f4_trump = (' '.join(value for value in lsi_feature4_array_trump) for n in range(50000))
stat_f1_clinton = (' '.join('%s:%s' % (key, value) for (key, value) in zip(vocabulary_unigram_clinton, unigram_feature1_array_clinton[n, :].toarray().reshape(len(vocabulary_unigram_clinton))) if value>0) for n in range(50000))
stat_f2_clinton = (' '.join('%s:%s' % (key, value) for (key, value) in zip(vocabulary_unigram_clinton, unigramtfidf_feature2_array_clinton[n, :].toarray().reshape(len(vocabulary_unigram_clinton))) if value>0) for n in range(50000))
stat_f3_clinton = (' '.join('%s:%s' % (key, value) for (key, value) in zip(vocabulary_normal_clinton, normaltfidf_feature3_array_clinton[n, :].toarray().reshape(len(vocabulary_unigram_clinton))) if value>0) for n in range(50000))
stat_f4_clinton = (' '.join(value for value in lsi_feature4_array_clinton) for n in range(50000))

with open("trump_result.csv", 'wb') as fileout:
    writer = csv.writer(fileout)
    writer.writerow(
        ["id", "result_feature_1", "result_feature_2", "result_feature_3", "result_feature_4", "feature_1", "feature_2",
         "feature_3", "feature_4"])
    writer.writerows(
        zip(id, unigram_feature1_array_trump_predict_result, unigramtfidf_feature2_array_trump_predict_result,
            normaltfidf_feature3_array_trump_predict_result, lsi_feature4_array_trump_predict_result, stat_f1_trump, stat_f2_trump, stat_f3_trump,
            stat_f4_trump))
    fileout.flush()

with open("clinton_result.csv", 'wb') as fileout:
    writer = csv.writer(fileout)
    writer.writerow(
        ["id", "result_feature_1", "result_feature_2", "result_feature_3", "result_feature_4", "feature_1", "feature_2",
         "feature_3", "feature_4"])
    writer.writerows(
        zip(id, unigram_feature1_array_clinton_predict_result, unigramtfidf_feature2_array_clinton_predict_result,
            normaltfidf_feature3_array_clinton_predict_result, lsi_feature4_array_clinton_predict_result, stat_f1_clinton, stat_f2_clinton,
            stat_f3_clinton, stat_f4_clinton))
    fileout.flush()
