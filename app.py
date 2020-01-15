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
    st.markdown("> W tej alikacji mozesz przeanalizowac dane pochodzace  z terapii iWakka")

    st.write("W aplikacji znajduje sie kilka sekcji: ")
    st.header("II. Pobierz dane")
    
    st.header(" III. Wprowadz notatki")
       
    st.header(" IV. Zobacz dane")

    st.header(" V. Porownaj pacjentow")
  
def create_layout() -> None:
    """
    Create the layout of dashboard
    
    """

    st.sidebar.title("Wybierz sekcje")
    app_mode = st.sidebar.selectbox("Please select a page", [' I. Strona domowa',
                                                             "II. Pobierz dane",
                                                             "III. Wprowadz notatki",
                                                             " IV. Zobacz dane",
                                                            " V. Porownaj pacjentow"])
    
    if app_mode == ' I. Strona domowa':
       load_homepage()       
    elif app_mode == " IV. Zobacz dane":
        leyer.leyer()        
    elif app_mode == "II. Pobierz dane":
         download_data.download_data()      
    elif app_mode == "III. Wprowadz notatki":
       text_input.text_input()
    elif app_mode == " V. Porownaj pacjentow":
       rank_of_patient.rank_of_patient()
        
    
if __name__ == "__main__":
    main()


    

