import csv
import re
import codecs
from nltk.tokenize import TweetTokenizer

def pre_processing(readfilename,writefileneme):
    tknzr = TweetTokenizer()
    with open(readfilename) as infile, codecs.open(writefileneme,'wb','utf-8') as outfile:
        reader = csv.reader(infile)
        reader.next()
        tweets = (row[-1] for row in reader)
        no_tag = (re.sub('<[^>]+>','',tweet) for tweet in tweets)
        no_link = (re.sub('(?:http|ftp|www)\S+','',tweet) for tweet in no_tag)
        no_at = (re.sub('@','',tweet).strip() for tweet in no_link)
        no_hash = (re.sub('(?: #\S+)+$','',tweet) for tweet in no_at)
        tokens = (tknzr.tokenize(tweet.lower()) for tweet in no_hash)
        lines = (" ".join(token)+"\n" for token in tokens)
        outfile.writelines(lines)
        outfile.flush()

