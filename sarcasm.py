
import pandas as pd 
import nltk
nltk.download('stopwords')  #Uncomment if stopwords aren't already dowloaded 
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


path = "C:/News Headline/dataset.json"

try:
    
    dataset = pd.read_json(path,lines = True)
    
    dataset = dataset.drop("article_link", axis = 1)
    
    X = dataset.headline
    y = dataset.is_sarcastic
    
    corpus = []
    print("The process will take time be patient!")
    for i in range(0,len(X)):
        review = re.sub('[^a-zA-Z]', ' ', X[i])
        review = review.lower()
        review = review.split()
        ps = PorterStemmer()
        review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
        review = ' '.join(review)
        corpus.append(review)
        print(i)

except:
        print("the file path i does'nt contain a json file")
        print("check the path.")
        