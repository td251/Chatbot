import nltk 
import numpy as np 
import random 
import string #to process standard  python strings 
import codecs
import io 
from sklearn.feature_extraction.text import TfidfVectorizer #convert a collection of raw documents to a matrix 
from sklearn.metrics.pairwise import cosine_similarity #cosine simalirity 

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
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def normalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
Greetings = ("Hello","Hi","YO","Yo","Heyo","Hey","Sup","Hello","Wag1","Greetings","wys","wassup",)
GreetingResponses = ["hi","hey", "Yo g", "How Goes it", "HEYO", "Talk to me", "Hi", "Ah youre finally talking to me", "Hey what you up to", "Hey need any help"]
def greeting(sentence): 

    for word in sentence.split():
        if word.lower() in Greetings:
            return random.choice(GreetingResponses)

def response(userRespons):
    bot_response='Chatbot: '
    listOfSentences.append(user_response)

    revelance = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    tfidf = revelance.fit_transform(listOfSentences) 
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten() 
    flat.sort() 
    req_tfidf = flat[-2]

    if(req_tfidf==0):
        bot_response=bot_response+"Tyler: Sorry, what do you mean?"

        return bot_response
    else:
        bot_response = bot_response+listOfSentences[idx]
        return bot_response

flag=True 
print("Tyler: Hi! My Name is Tyler, if you wish to exit please type bye.")

while(flag==True):
    user_response = raw_input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("Chatbot: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("Chatbot: "+greeting(user_response))
            else:
                # print("ROBO: ",end="")
                print(response(user_response))
                listOfSentences.remove(user_response)
    else:
        flag=False
        print("ROBO: Bye! take care..")