# -*- coding: utf-8 -*-


import streamlit as st
import pandas as pd

def text_input() -> None:
    """
  
    Create the layout, adding buttons and widgets to this  ' IV. Notes'  dashboard's section
   
    Take some notes about selected patient and specify the level of motivation anf fatigue on a 0-100 scale
    
    Returns:
    -----------
    
    Appends row to existing .csv file :
    |  ID      |  Motivation   |  Tiring   |  Condition     |  Notes          |
    |  ......  |  ......       |  .....    | .....          |  .....          | 
    |  ......  |  ......       |  .....    | .....          |  .....          |    
    |  ......  |  ......       |  .....    | .....          |  .....          |   
    |  BKZI    |   55          |   30      |   80           |  glasses needed |      
    
    
    
    """
    
    st.header(" Tutaj mozesz wprowadzic notatki dotyczace pacjentow")
#    st.markdown("Some notes can be useful for you, it's too hard to remeber all inormation about your patient :)")
    
    
    patient_IDs= ['BKZI', 'MAMCZ', 'Anna Dzialak', 'ASCZ', 'BBZI', 'BMCZ', 'KKZI'
                , 'DMCZ', 'EKZI', 'ELCZ', 'HKZI','JKCZ', 'JRCZ', 'JSCZ' , 
                  'MBCZ', 'MMCZ', 'MPCZ', 'RKZI', 'SBZI' , 'UNZI', 'ZPZI']
    a =st.text_input('Jezeli lista nie zawiera jakiegos pacjenta, mozesz go dodac tutaj')
    patient_IDs.append(a)    
    c =st.checkbox('Pokaz liste pacjentow')
    if c:
        st.show(patient_IDs)
    #st.show(ID)
    option = st.selectbox(
            'Wybierz pacjenta',patient_IDs
    )
    for i in patient_IDs:
        if option == i:
            notes = st.text_input(('Mozesz wprowadzic jakies notatki dla %s')%(i))
#           ade1= st.slider('How much {} is motivaed?'.format(i))
            ade11= st.slider('Jak bardzo {} jest zmotywowany'.format(i),
                        0, 100)
            st.write('Wartosc:', ade11)

            age2= st.slider('Jaki jest stan zdrowia {} ?'.format(i),
                        0, 100 )
            st.write('Wartosc:', age2)

            age3 = st.slider('Czy {} narzeka podczas cwiczen?'.format(i),
                        0, 100)
            st.write('Wartosc:', age3)
            
            age4 = st.slider('Jak bardzo {} jest zmeczony?'.format(i),
                        0, 100) 
            st.write('Wartosc:', age4)
            
#            data = {i : [adek]}
#            data=pd.DataFrame.from_dict(data, orient='columns', dtype=None)
#            st.show(data)
            data = [[i, ade11, age2, age3, age4, notes]] 
  
# Create the pandas DataFrame 
            df = pd.DataFrame(data, columns = ['ID', 'Motywacja', 'Stan pacjenta', 'Narzekanie', 'Zmeczenie', 'Notatki']) 

          
            if st.button('dodaj wprowadzone informacje '):
                with open('notes.csv','a') as fd:
                     df.to_csv(fd, header=False)
            g=pd.read_csv('notes.csv')
            st.write('data', g)