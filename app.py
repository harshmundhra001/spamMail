import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'));
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))


st.title('Email/SMS Spam Classifier')

input_sms = st.text_input("Enter the message")

if st.button('Predict'):

    vector_input = tfidf.transform([input_sms])

    result = model.predict(vector_input)[0]

    if result == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')