import streamlit as st
import pickle

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load Model
model = load_model("lstm_sentiment_model.h5")

# Load Tokenizer
tokenizer = pickle.load(open("tokenizer.pkl","rb"))

st.title("🎬 Movie Review Sentiment Analyzer")

review = st.text_area("Enter your movie review")

if st.button("Predict Sentiment"):

    seq = tokenizer.texts_to_sequences([review])

    padded = pad_sequences(seq,maxlen=200)

    prediction = model.predict(padded)

    if prediction[0][0] > 0.5:
        st.success("Positive Review 😀")
    else:
        st.error("Negative Review 😡") 