#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 21:08:16 2020

@author: anna
"""

# Python code demonstrate creating  
# DataFrame from dict narray / lists  
# By default addresses. 
import sys
import pandas as pd
import altair as alt  
import streamlit as st
import urllib

# Create DataFrame 
def leerer():
    
    def get_UN_data():
        df = pd.read_csv('https://raw.githubusercontent.com/209614-student/streamlit_iWakka/master/document.csv')
        return df.set_index("ID")
    
    try:
        df = get_UN_data()
    except urllib.error.URLError as e:
        st.error(
            """
            **This demo requires internet access.**
    
            Connection error: %s
        """
            % e.reason
        )
    
    countries = st.multiselect(
        "Choose countries", list(df.index), ['HKZI', 'BBZI']
    )
    
    data = df.loc[countries]
    if st.checkbox('show data'):
        st.write("Wyniki AGF", data.sort_index())
    data = data.T.reset_index()
    data = pd.melt(data, id_vars=["index"]).rename(
        columns={"index": "day", "value": "Wyniki AGF"}
    )
    a= alt.Chart(data).mark_bar().encode(
                x='day:O',
                y="Wyniki AGF:Q",
                # The highlight will be set on the result of a conditional statement
                color=alt.condition(
                        alt.datum.year == 1810,  # If the year is 1810 this test returns True,
                        alt.value('orange'),     # which sets the bar orange.
                        alt.value('steelblue')   # And if it's not true it sets the bar steelblue.
                        )
                ).properties(width=600)

    st.write("", "", a)