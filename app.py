import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def tranform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
            
    text = y[:]
    y.clear() 
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
        
    return " ".join(y) 

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS spam classifier")

input_sms = st.text_input("Enter the message")

if st.button('predict'):
    #Ther are 4 steps
    # 1preprocess
    transformed_sms = tranform_text(input_sms)
    # 2vectorizer
    vector_input = tfidf.transform([transformed_sms])
    # 3predict
    result = model.predict(vector_input)[0]
    # 4display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
 

 # streamlit run app.py is command use to run this project
 