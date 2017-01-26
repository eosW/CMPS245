import csv
import re
from nltk.tokenize import word_tokenize

def pre_processing(readfilename,writefileneme):
    with open(readfilename) as infile, open(writefileneme,'wb') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        reader.next()
        tweets = (row[-1] for row in reader)
        no_tag = (re.sub('<[^>]+>','',tweet) for tweet in tweets)
        no_link = (re.sub('(?:http|ftp|www)\S+','',tweet) for tweet in no_tag)
        no_at = (re.sub('@','',tweet) for tweet in no_link)
        no_hash = (re.sub('(?: #\S+)+$','',tweet) for tweet in no_at)
        tokens = (word_tokenize(tweet.lower()) for tweet in no_hash)
        writer.writerows(tokens)
        outfile.flush()

