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
    
    st.header(" Hello again! In this section you cen provide some notes regarding patient")
    st.markdown("Some notes can be useful for you, it's too hard to remeber all inormation about your patient :)")
    
    
    patient_IDs= ['BKZI', 'MAMCZ', 'Anna Dzialak', 'ASCZ', 'BBZI', 'BMCZ', 'KKZI'
                , 'DMCZ', 'EKZI', 'ELCZ', 'HKZI','JKCZ', 'JRCZ', 'JSCZ' , 
                  'MBCZ', 'MMCZ', 'MPCZ', 'RKZI', 'SBZI' , 'UNZI', 'ZPZI']
    a =st.text_input('If list does not contain any ID, you can add it')
    patient_IDs.append(a)    
    c =st.checkbox('Show existing patient ID lists')
    if c:
        st.show(patient_IDs)
    #st.show(ID)
    option = st.selectbox(
            'Which patient would you like to choose?',patient_IDs
    )
    for i in patient_IDs:
        if option == i:
            notes = st.text_input(('You can provide some notes %s')%(i))
#           ade1= st.slider('How much {} is motivaed?'.format(i))
            ade11= st.slider('How much {} is motivated'.format(i),
                        0, 100)
            st.write('Range values:', ade11)

            age2= st.slider('What is {} condition?'.format(i),
                        0, 100 )
            st.write('Range values:', age2)

            age3 = st.slider('Does {} complain?'.format(i),
                        0, 100)
            st.write('Range values:', age3)
            
            age4 = st.slider('How mach {} is tired'.format(i),
                        0, 100) 
            st.write('Range values:', age4)
            
#            data = {i : [adek]}
#            data=pd.DataFrame.from_dict(data, orient='columns', dtype=None)
#            st.show(data)
            data = [[i, ade11, age2, age3, age4, notes]] 
  
# Create the pandas DataFrame 
            df = pd.DataFrame(data, columns = ['ID', 'Motivation', 'Condition', 'Complains', 'Tiring', 'Notes']) 

          
            if st.button('append'):
                with open('notes.csv','a') as fd:
                     df.to_csv(fd, header=False)
            g=pd.read_csv('notes.csv')
            if st.checkbox('show data'):
                st.write('data', g)