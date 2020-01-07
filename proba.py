import pandas as pd
import streamlit as st

def proba():
    df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
                        'mask': ['red', 'purple'],
                       'weapon': ['sai', 'bo staff']})
    a = df.to_csv(index=False)
    export_csv = df.to_csv (r'/home/anna/data/export_dataframe.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path
    
    g= pd.read_csv('/home/anna/data/export_dataframe.csv')
    
    
    st.write('data', g)
proba()