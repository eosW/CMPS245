from preprocess import pre_processing
from feature_generation import feature_extraction

tag_nonormal = "no_normal"
tag_normal = "normal"
#pre_processing("trump-50k.csv","trump_tokens_nonormal.csv", tag_nonormal)
#pre_processing("clinton-50k.csv","clinton_tokens_nonormal.csv", tag_nonormal)
feature_extraction("trump_nonormal_tokens.csv", "trump_tokens_feature_tfidf.csv")
feature_extraction("clinton_nonormal_tokens.csv", "clinton_tokens_feature_tfidf.csv")
