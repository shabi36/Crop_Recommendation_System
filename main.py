
import streamlit as st
import pickle
import numpy as np

dataset = pickle.load(open("CROP_DATASET.pkl", "rb"))
pipe = pickle.load(open("pipe_crop.pkl", "rb"))


st.title("CROP RECOMMENDATION SYSTEM ")

col1 , col2 , col3 = st.columns(3)

with col1:
    nit = st.number_input("Nitrogen (mg/kg)")

with col2:
    pot = st.number_input("Potassium (mg/kg)")

with col3:
    phos = st.number_input("Phosphorus (mg/kg")




col1 , col2  = st.columns(2)

with col1:
    temp = st.number_input("Temperature (C)")

with col2:
    humi = st.number_input("Humidity")


col1 , col2  = st.columns(2)

with col1:
    ph = st.number_input("pH")

with col2:
    rpm = st.number_input("Rainfall per month (mm)")


if st.button("Recommend Crop"):

    query = np.array([nit,pot,phos,temp,humi,ph,rpm])

    query = query.reshape(1, 7)

    x = pipe.predict(query)[0]

    crops = ["Banana" , "Blackgram" , "Chickpea" , "Coconut" , "Coffee",
             "Cotton" , "Grapes" , "Groundnuts" , "Jute" , "Kidneybeans",
             "Lentil", "Maize", "Mango", "Mothbeans" , "Mungbean",
             "Muskmelon", "Orange" , "Papaya" , "Pigeonpeas" , "Pomegranate",
             "Rice","Watermelon"]

    st.title(crops[x])