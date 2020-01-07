# -*- coding: utf-8 -*-

import streamlit as st
#import checkboc_pacjenci
import leyer
import text_input
import numpy as np
#import untitled0
import dataex
import download_data
import proba
#import data_processing

def main():
    create_layout()
    
def load_homepage() -> None:
    st.image("https://raw.githubusercontent.com/209614-student/streamlit_iWakka/master/iwakka.png",
             use_column_width=True)
    st.markdown("> It' s a dashboard do analize data!")
    st.write("Hello! This dashboard will help you to analize data from our device iWakka "
             "This app will help your patient to recovery ")

    st.write("Here are some step to process data: ")
    st.header(" II. Download data")
    st.write("It is first step for you to click bottom and gather data from e-mail")
    
    st.header(" III. In this section you can provide some notes")
    st.write("It can be useful for you to collect notes concerning your patient")   
       
    st.header(" IV. Expore AGF score for patient")
    st.write("You can judge patient condition accroding to provided data")      

    st.header(" V. You will find rank if patients")
    st.write("You can judge patient condition accroding to provided data")         
  
def create_layout():

    

    st.sidebar.title("Menu")
    app_mode = st.sidebar.selectbox("Please select a page", [' I. Homepage',
                                                             "II. Download data" ,
                                                             "III. Statistic Data",
                                                             ' IV. Notes',
                                                             " V. Rank of patient"])
    
    if app_mode == ' I. Homepage':
       load_homepage()
       
    elif app_mode == "III. Statistic Data":
        leyer.leerer()
        
    elif app_mode == "II. Download data":
         download_data.download_data()
      
    elif app_mode == ' IV. Notes':
       text_input.text_input()
    elif app_mode == " V. Rank of patient":
       proba.proba()
        
    
if __name__ == "__main__":
    main()


    

