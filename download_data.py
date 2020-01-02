# -*- coding: utf-8 -*-


import pandas as pd
import streamlit as st
import numpy as np


def download_data(): 
    reka_chora= pd.read_csv('https://raw.githubusercontent.com/209614-student/streamlit_iWakka/master/document.csv')
   # reka_zdrowa = 
    st.write('Data', reka_chora)

"""
def download_data():
#    data = pd.read_csv("reka_chora.csv")
    st.header(" It's actually first step to start process data of your patient.")
    st.header(" Just follow the instruction!")
    st.markdown("Hi! It's fisrt step! Just click the bottom below and download data!")
    button =st.button('START DOWNLOAD DATA')
    if button:
       download_dataraw() 
    st.write ('Atfter downloading data, you can press the button below to start processing them!')
    add=st.text_input('dodaj ID')
    
    ID = ['BKZI','ZPZI','HKZI','BBZI','SBZI','DMCZ','JRCZ','JKCZ']
    ID.append(add)
    option = st.selectbox(
            'Which patient would you like to choose?',ID
    )
    for i in ID:
        if option == i:
            patient_ID = i
            button2 = st.button('START PROCESSING DATA')
            if button2:
                data_processing(patient_ID)

"""