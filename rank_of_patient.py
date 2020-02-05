# -*- coding: utf-8 -*-


import altair as alt
import pandas as pd
import streamlit as st

def rank_of_patient():
    
    st.header(" You can compare results for selected patients")
    """
    Create the layout after the data has succesfully loaded, adding buttons and widgets to this  " V. Rank of patient" dashboard's section
    
    
    Returns:
    -----------
    chart: chart
        chart to visualize and compare the AGF results for selected patients 
    
    
    """
    def get_UN_data():
            df = pd.read_csv('./data/document1.csv')
            df['Total']=df.sum(axis = 1, skipna = True)
            return df.set_index("ID")
        
    df = get_UN_data()

    
    countries = st.multiselect(
        "Choose ID", list(df.index), ['HKZI', 'BBZI', 'BKZI','MAMCZ','SBZI', 'JRCZ']
    )
    
    data = df.loc[countries]
    data = data.sort_index()
    data = data.reset_index()
    #data = pd.melt(data, id_vars=["index"]).rename(
    #    columns={"index": "ID"}
    #)
    a= alt.Chart(data).mark_bar().encode(
                x='ID:O',
                y="Total:Q",
                # The highlight will be set on the result of a conditional statement
                color=alt.condition(
                        alt.datum.year == 1810,  # If the year is 1810 this test returns True,
                        alt.value('orange'),     # which sets the bar orange.
                        alt.value('steelblue')   # And if it's not true it sets the bar steelblue.
                        )
                ).properties(width=600)
    
    st.write("", "", a)
