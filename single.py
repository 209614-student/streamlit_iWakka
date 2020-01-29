#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:04:01 2020

@author: anna
"""
import altair as alt
import pandas as pd
import streamlit as st
import glob

def AGF_indices():
    st.header(" This panel alows you to analize every chart from therapy for selected patients")

    patient_IDs= ['BKZI', 'MAMCZ', 'Anna Dzialak', 'ASCZ', 'BBZI', 'BMCZ', 'KKZI'
                    , 'DMCZ', 'EKZI', 'ELCZ', 'HKZI','JKCZ', 'JRCZ', 'JSCZ' , 
                      'MBCZ', 'MMCZ', 'MPCZ', 'RKZI', 'SBZI' , 'UNZI', 'ZPZI']
    mode = st.selectbox("Please select ID", patient_IDs)
    st.write("It can be take some minutes")
    CODE_SHEET = pd.read_excel('./data/code_ocena_1.xlsx')
    def find_data(patient_ID: str) ->str:
        """
    
        Parameters:
        -----------
        patient_ID : str
                The nick of patient      
    
        Returns:
        -----------                
    
        list
            list of loaded .csv files by pandas.read_csv command from ./data folder
    
        """
        path='./data/*'    
        files = glob.glob(path)
        file_list = []
        for i, file_name in enumerate(files):
            file_list.append(file_name)
            file_list=sorted(file_list)
    
        result_sheets = []
        for file_path in file_list:
            if  file_path.find(str(patient_ID)) > -1: 
                result_sheet = pd.read_csv(file_path )
                result_sheets.append(result_sheet )
    
        return result_sheets 
    
    
    if mode:
        patient_ID = mode
        result_sheets=find_data(str(patient_ID))
    
    def computed(result_sheet:list) -> list:
        """
        The function returns a list containing the AGF value, each number corresponds to one measurement, i.e. the result of one day
        Function usues code_ocena_1.xlsx temlete due to measure AGF value only from this part wchich corresponds with grasping and releasing movements
        
        Parameters:
        -----------
         
        list
            list of loaded .csv files by pandas.read_csv command from ./data folder
        
         Returns:
        ---------
        evaluation: list
            list of number - AGF score from every single measurement
                
        """
        deviation = abs(result_sheet['value[g]'] - result_sheet['target[g]'])
        sampling_time = []
        for i in result_sheet['time[s]'].index:
            if i < 1300:
                sampling_time.append(result_sheet['time[s]'][i+1]-result_sheet['time[s]'][i])
        sampling_time.append(0)
        
        error_area = []
        for i in result_sheet['time[s]'].index:
            if i < 1300:
                error_area.append((deviation[i+1] + deviation[i])/2*sampling_time[i])
                
        error_area.append(0)
        
        evaluation = {'IC':0, 'CC1':0, 'CC2':0, 'CC3':0, 'CC4':0, 'CC5':0, 'CC6':0, 'CC7':0, 'CC8':0, 'CC9':0, 'CC10':0, 'EC1':0, 
                 'EC2':0, 'EC3':0, 'EC4':0, 'EC5':0, 'EC6':0, 'EC7':0, 'EC8':0, 'EC9':0, 'EC10':0, 'Total':0}
        for i in result_sheet['time[s]'].index:
            if i < 1300:
                if CODE_SHEET['code_number'][i] == 1:
                    evaluation['IC'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 2:
                    evaluation['CC1'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 3:
                    evaluation['CC2'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 4:
                    evaluation['CC3'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 5:
                    evaluation['CC4'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 6:
                    evaluation['CC5'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 7:
                    evaluation['CC6'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 8:
                    evaluation['CC7'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 9:
                    evaluation['CC8'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 10:
                    evaluation['CC9'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 11:
                    evaluation['CC10'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 12:
                    evaluation['EC1'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 13:
                    evaluation['EC2'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 14:
                    evaluation['EC3'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 15:
                    evaluation['EC4'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 16:
                    evaluation['EC5'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 17:
                    evaluation['EC6'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 18:
                    evaluation['EC7'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 19:
                    evaluation['EC8'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 20:
                    evaluation['EC9'] += error_area[i]
                    evaluation['Total'] += error_area[i]
                elif CODE_SHEET['code_number'][i] == 21:
                    evaluation['EC10'] += error_area[i]
                    evaluation['Total'] += error_area[i]           
        # divide by time
        evaluation['IC'] = evaluation['IC']/5
        evaluation['Total'] = evaluation['Total']/65
        for eval_unit in evaluation:
            if eval_unit != 'IC' and eval_unit != 'Total':
                evaluation[eval_unit] = evaluation[eval_unit]/3
        print(evaluation['IC'],evaluation['CC1'],evaluation['Total' ] )  
        a= list(evaluation.values())
        print (a)
        return  a
           
    a=computed(result_sheets[1])
    
    
    for i in result_sheets:
        a=computed(i)    
        source = pd.DataFrame({
            'AGF Indices': ['IC', 'CC1', 'CC2', 'CC3', 'CC4', 'CC5', 'CC6', 'CC7', 'CC8', 'CC9', 'CC10', 'EC1', 
                         'EC2', 'EC3', 'EC4', 'EC5', 'EC6', 'EC7', 'EC8', 'EC9', 'EC10', 'Total'] ,
            'AGF Score': a
        })
        c = alt.Chart(source).mark_bar().encode(
            x=alt.X('AGF Indices', sort=None),
            y='AGF Score'
        )
          
        st.write('Data', c)
        
            
        
        
