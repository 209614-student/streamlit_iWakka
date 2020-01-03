#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:03:56 2019

@author: anna
"""

import streamlit as st
import numpy as np
import pandas as pd

def text_input():

    
    st.header(" Hello again! In this section you cen provide some notes regarding patient")
    st.markdown("Some notes can be useful for you, it's too hard to remeber all inormation about your patient :)")
    
    
    ID = ['BKZI','ZPZI','HKZI','BBZI','SBZI','DMCZ','JRCZ','JKCZ']
    #st.show(ID)
    option = st.selectbox(
            'Which patient would you like to choose?',ID
    )
    for i in ID:
        if option == i:
            title = st.text_input(('You can provide some notes %s')%(i))
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
            
            
