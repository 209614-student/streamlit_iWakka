# -*- coding: utf-8 -*-

import pandas as pd
import altair as alt  
import streamlit as st

def leyer() -> None:
    """
    Create the layout after the data has succesfully loaded, adding buttons and widgets to this  "III. Statistic Data"  dashboard's section
    
    
    Returns:
    -----------
    chart: chart
        chart to visualize the AGF result for each day of therapy using the altair library
    
    
    """
    def get_UN_data() -> None :
        df = pd.read_csv('./data/document1.csv')
        return df.set_index("ID")

    df = get_UN_data()
   
    mode = st.selectbox("Please select ID", list(df.index))
    for i in list(df.index):
        if mode == i:
            data = df.loc[i]
            data = data.T.reset_index()
            data = pd.melt(data, id_vars=["index"]).rename(
                columns={"index": "day", "value": "AGF score"}
            )
            chart =   alt.Chart(data).mark_bar().encode(
                            x=alt.Y('day:O', sort = None),
                            y=alt.Y("AGF score:Q"),
                            color=alt.condition(
                                    alt.datum.year == 1810,  # If the year is 1810 this test returns True,
                                    alt.value('orange'),     # which sets the bar orange.
                                    alt.value('steelblue')   # And if it's not true it sets the bar steelblue.
                                    )
                            ).properties(width=600)
           
            st.write("Chart", chart)
                            
            
