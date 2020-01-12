# -*- coding: utf-8 -*--

import streamlit as st
import leyer
import text_input
import rank_of_patient
import download_data

def main():
    create_layout()
    
def load_homepage() -> None:
    """    The homepage is loaded using a combination of .write and .markdown.
    
           Contains description how app works 
        
    """
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
  
def create_layout() -> None:
    """
    Create the layout of dashboard
    
    """

    st.sidebar.title("Menu")
    app_mode = st.sidebar.selectbox("Please select a page", [' I. Homepage',
                                                             "II. Download data" ,
                                                             "III. Statistic Data",
                                                             ' IV. Notes',
                                                             " V. Rank of patient"])
    
    if app_mode == ' I. Homepage':
       load_homepage()       
    elif app_mode == "III. Statistic Data":
        leyer.leyer()        
    elif app_mode == "II. Download data":
         download_data.download_data()      
    elif app_mode == ' IV. Notes':
       text_input.text_input()
    elif app_mode == " V. Rank of patient":
       rank_of_patient.rank_of_patient()
        
    
if __name__ == "__main__":
    main()


    

