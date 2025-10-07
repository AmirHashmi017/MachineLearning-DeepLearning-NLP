import streamlit as st
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

model= load_model('next_word_lstm.h5')

with open('tokenizer.pkl','rb') as file:
    tokenizer= pickle.load(file)

max_sequence_len= model.input_shape[1]+1

def predict_next_word(model,tokenizer,text,max_sequence_len):
    token_list=tokenizer.texts_to_sequences([text])[0]
    if len(token_list)>=max_sequence_len:
        token_list=token_list[-(max_sequence_len-1):]
    token_list= pad_sequences([token_list],maxlen=max_sequence_len-1,padding='pre')
    predicted= model.predict(token_list,verbose=0)
    predicted_word_index=np.argmax(predicted,axis=1)
    for word,index in tokenizer.word_index.items():
        if index== predicted_word_index:
            return word

## Streamlit App
st.title("Next Word Prediction")

user_input = st.text_area(label="Enter your text here")

predicted_word= predict_next_word(model,tokenizer,user_input,max_sequence_len)

if st.button("Predict Next Word"):
    st.write(f"Next Word: {predicted_word}")