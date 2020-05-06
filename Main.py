import nltk 
import numpy as np 
import random 
import string #to process standard  python strings 
import codecs
import io 

# f= codecs.open('chatbot.txt','r',errors = 'ignore')
f = io.open('chatBot.txt', 'rU', encoding='utf-8')    
dataset= f.read() 
dataset=dataset.lower() #converts to lowercase 
nltk.download('punkt') # first time use only 
nltk.download('wordnet') # first time use only 
listOfSentences = nltk.sent_tokenize(dataset) #converts to list of sentences 
listOfWords = nltk.word_tokenize(dataset)# converts to list of words 
# wordnet is a semantically proented dictionary of english included in nltk
lemmer = nltk.stem.WordNetLemmatizer() 
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
removePunctuation