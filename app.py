# -*- coding: utf-8 -*--

import streamlit as st
import leyer
import text_input
import rank_of_patient
import download_data
import single

def main():
    create_layout()
    
def load_homepage() -> None:
    """    The homepage is loaded using a combination of .write and .markdown.
    
           Contains description how app works 
        
    """
    st.image("iwakka.png",
             use_column_width=True)
 
    st.header("Hello! This dashboard will help you to analize data from iWakka device")
    st.write("Here are some step to process data: ")
    st.header(" II. Download data")
    st.write("Here you can download data")
    
    st.header(" III. Statistic Data")
    st.write("You can judge patient condition accroding to provided data")     
         
    st.header("IV. AGF Indices")
    st.write("Here you can analyse each chart")      
      
    st.header("  V. Notes")
    st.write("It can be useful for you to collect notes concerning your patient")   

    st.header(" VI. Rank of patient")
    st.write("You can compare results for selected patients" )         
  
def create_layout() -> None:
    """
    Create the layout of dashboard
    
    """

    st.sidebar.title("Menu")
    app_mode = st.sidebar.selectbox("Please select a page", [' I. Homepage',
                                                             "II. Download data" ,
                                                             "III. Statistic Data",
                                                             ' IV. AGF Indices',
                                                             ' V. Notes',
                                                             " VI. Rank of patient"  ])
    
    if app_mode == ' I. Homepage':
       load_homepage()       
    elif app_mode == "III. Statistic Data":
        leyer.leyer()     
    elif app_mode == ' IV. AGF Indices':
        single.AGF_indices()   
    elif app_mode == "II. Download data":
         download_data.download_data()      
    elif app_mode == ' V. Notes':
       text_input.text_input()
    elif app_mode == " VI. Rank of patient":
       rank_of_patient.rank_of_patient()
        
    
if __name__ == "__main__":
    main()


    

