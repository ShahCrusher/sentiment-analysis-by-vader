import pandas
import numpy
import nltk
import streamlit as st

from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm

sia = SentimentIntensityAnalyzer()
def senti(text):
    result = sia.polarity_scores(text)['compound']
    if result > 0.05:
        st.header('Happy 😀')
    elif result < -0.05:
        st.header('Sad 😡')
    elif result >= -0.05 and result <= 0.05:
        st.header('No Emotion 😐')
    
st.header('Sentiment Analysis')
text = st.text_area('Please Enter your message')
if st.button('Submit'):
    senti(text)