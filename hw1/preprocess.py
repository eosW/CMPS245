
import csv
import re
import string
from nltk.tokenize import TweetTokenizer
from nltk.stem import RSLPStemmer
import nltk
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def pre_processing(readfilename, writefileneme, tag):    
    stop_words_list = []
    stopwords_file = "google_stopwords"
    for temp_word in open(stopwords_file, 'r'):
        stop_words_list.append(temp_word.replace("\n", ""))
    tknzr = TweetTokenizer()
    with open(readfilename) as infile, open(writefileneme,'wb') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        reader.next()
        tweets = (row[-1] for row in reader)
        no_tag = (re.sub('<[^>]+>','',tweet) for tweet in tweets)
        no_link = (re.sub('(?:http|ftp|www)\S+','',tweet) for tweet in no_tag)
        no_at = (re.sub('@','',tweet).strip() for tweet in no_link)
        no_hash = (re.sub('(?: #\S+)+$','',tweet) for tweet in no_at)
        
        no_punc = ((tweet.translate(string.maketrans("",""),string.punctuation)) for tweet in no_hash)
        #for tweet in no_hash:
        #    new_tweet = tweet.translate(string.maketrans("",""),string.punctuation)
        #    print new_tweet
        st = RSLPStemmer()
        if tag == "no_normal":
            tokens = (tknzr.tokenize(tweet) for tweet in no_punc)
        if tag == "normal":
            no_punc_fileter_stop = []
            tweet_num = 0
            for tweet_notlower in no_punc:
                tweet = tweet_notlower.lower()
                tweet_num += 1
                if tweet_num % 500 == 0:
                    print tweet_num
                temp_len = 0
                temp_words = tweet.split(" ")
                temp_sentence = ""
                temp_sentence_len = len(temp_words)
                for temp_single_word in temp_words:
                    temp_len += 1
                    if temp_single_word in stop_words_list:
                        pass
                    else:
                        if len(temp_single_word) != 0:   
                            if temp_len == temp_sentence_len:
                                temp_sentence += st.stem(temp_single_word)
                            else:
                                temp_sentence += st.stem(temp_single_word) + " "
                #print temp_sentence
                no_punc_fileter_stop.append(temp_sentence)
            tokens = (tknzr.tokenize(tweet.lower()) for tweet in no_punc_fileter_stop)
        writer.writerows(tokens)
        
        outfile.flush()
