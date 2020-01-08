#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import altair as alt  
import streamlit as st
import urllib

def leyer():
    def get_UN_data():
        df = pd.read_csv('./data/document1.csv')
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
    #countries = st.multiselect(
     #   "Choose countries", list(df.index), ['HKZI']
    #)
    
    
    mode = st.selectbox("Please select ID", list(df.index))
    for i in list(df.index):
        if mode == i:
            data = df.loc[i]
            data = data.T.reset_index()
            data = pd.melt(data, id_vars=["index"]).rename(
                columns={"index": "day", "value": "Wyniki AGF"}
            )
            a =   alt.Chart(data).mark_bar().encode(
                            x=alt.Y('day:O', sort = None),
                            y=alt.Y("Wyniki AGF:Q"),
                            color=alt.condition(
                                    alt.datum.year == 1810,  # If the year is 1810 this test returns True,
                                    alt.value('orange'),     # which sets the bar orange.
                                    alt.value('steelblue')   # And if it's not true it sets the bar steelblue.
                                    )
                            ).properties(width=600)
           
            st.write("Chart", a)
                            
            
