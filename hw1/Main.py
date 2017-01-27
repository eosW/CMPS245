#from preprocess import pre_processing
from feature_generation import feature1_unigram_extraction
from feature_generation import feature2_unigram_tfidf_extraction
from feature_generation import feature3_normal_tfidf_extraction
from feature_generation import feature4_lsi_extraction

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
unigram_feature1_array_trump = feature1_unigram_extraction(data_no_normal_trump)
unigram_feature1_array_clinton = feature1_unigram_extraction(data_no_normal_clinton)
unigramtfidf_feature2_array_trump = feature2_unigram_tfidf_extraction(unigram_feature1_array_trump)
unigramtfidf_feature2_array_clinton = feature2_unigram_tfidf_extraction(unigram_feature1_array_clinton)
normaltfidf_feature3_array_trump = feature3_normal_tfidf_extraction(data_normal_trump)
normaltfidf_feature3_array_clinton = feature3_normal_tfidf_extraction(data_normal_clinton)
lsi_feature4_array_trump = feature4_lsi_extraction(normaltfidf_feature3_array_trump)
lsi_feature4_array_clinton = feature4_lsi_extraction(normaltfidf_feature3_array_clinton)













