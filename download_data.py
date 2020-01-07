# -*- coding: utf-8 -*-


import pandas as pd
import streamlit as st


def download_data(): 
    st.header(" It's actually first step to start process data of your patient.")
    st.markdown("Hi! It's fisrt step! Just click the bottoms below and download data!")
    button =st.button('START DOWNLOAD DATA')
    if button:
       reka_chora= pd.read_csv('https://raw.githubusercontent.com/209614-student/streamlit_iWakka/master/document.csv')
       reka_zdrowa =  pd.read_csv('https://raw.githubusercontent.com/209614-student/streamlit_iWakka/master/document1.csv')
       st.write('Data for ill hand ', reka_chora)
       st.write('Data for health hand', reka_zdrowa)

"""
def download_data():


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