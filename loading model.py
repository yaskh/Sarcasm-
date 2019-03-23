import pickle
from keras.models import load_model
classifier = load_model('regularizer.h5')

vectorizer = pickle.load(open("vectorizer", 'rb'))
test = input("Enter sentence")

sentence = vectorizer.transform(test)

classifier.predict()

