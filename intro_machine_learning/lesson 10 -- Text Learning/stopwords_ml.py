# import nltk
# nltk.download() 
# download stopwords
from nltk.corpus import stopwords 

sw = stopwords.words("english")
print sw[0:11]
print len(sw)