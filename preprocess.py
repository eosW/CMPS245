
import csv
import re
import string
from nltk.tokenize import TweetTokenizer

def pre_processing(readfilename, writefileneme, tag):
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
        if tag == "no_normal":
            tokens = (tknzr.tokenize(tweet.lower()) for tweet in no_punc)
        if tag == "normal":
            tokens = (tknzr.tokenize(tweet.lower()) for tweet in no_punc)
        writer.writerows(tokens)
        outfile.flush()
