#!/usr/bin/env python
# coding: utf-8


""" This script is used to download attachment as .csv files which contains 'tch' in the titles from gmail sever on local computer in order to process them and use in project

"""


# import packages
import email
import imaplib
import os
import sys
import streamlit as st

def download_dataraw():
    """ Downloading e-mail attachments as .csv file into 'data folder'
        
        Printing out file names as strings.    
        
    """
    userName = '#########@gmail.com' # gmail login
    passwd = '###########' # gmail password
     #   directory = '/home/anna'      
    detach_dir = '.'
    if 'data' not in os.listdir(detach_dir):
        os.mkdir('data') 
    
    try:
        imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
        typ, accountDetails = imapSession.login(userName, passwd)
        if typ != 'OK':
            raise
    
        imapSession.select('Inbox')
        typ, data = imapSession.search(None, 'ALL')
        if typ != 'OK':
            
            raise
       
        for msgId in data[0].split():
            typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
     
            emailBody = messageParts[0][1]
            mail = email.message_from_bytes(emailBody)
            subject = mail['subject']
            if subject.find('tch')   > -1:
                for part in mail.walk():
                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get('Content-Disposition') is None:
                        continue
                    fileName = part.get_filename()
                    st.write(fileName)
    
                    if bool(fileName):
                        filePath = os.path.join(detach_dir, 'data', fileName)
                        if not os.path.isfile(filePath) :
                            print (fileName)
                            st.write(fileName)
                            fp = open(filePath, 'wb')
                            fp.write(part.get_payload(decode=True))
                            fp.close()
        imapSession.close()
        imapSession.logout()
    
        st.write ('Done')
        st.write ('Data has downloaded! Now you can press the button below to start processing them!')
 
    except :
        st.write ('Not able to download all attachments.')
download_dataraw()
        


import pandas as pd
import os
import glob
import numpy as np
import streamlit as st

import numpy as np
import numpy as np
def data_processing(patient_ID): 

    CODE_SHEET = pd.read_csv('https://raw.githubusercontent.com/209614-student/streamlit_iWakka/master/code_ocena_1.csv')
    # find excel files in directry whose name is from the argument(subject)
    def find_data(patient_ID):
        # find .xlsx in path
        path='/home/anna/data/*'    
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
    result_sheets=find_data(str(patient_ID))
        
    def computed(result_sheet):
        deviation = abs(result_sheet['value[g]'] - result_sheet['target[g]'])
        sampling_time = []
        previous_time = 0
        for i in result_sheet['time[s]'].index:
            if i < 1300:
                sampling_time.append(result_sheet['time[s]'][i+1]-result_sheet['time[s]'][i])
                previous_time = result_sheet['time[s]'][i]
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
                
        return evaluation
    
    def nwm():
        y=[]
        Y1=[]
        result_scheets= find_data(str(patient_ID ))
        for i in result_sheets:
            a=computed(i)['Total']
            a=np.round(a,3)
            y.append(a)
            Y1=[i for i in range(1,(len(y)+1))]  
        return y, Y1, patient_ID
    
    y, Y1, patient_ID= nwm()
       
    data = dict()
    for x in range(1,len(y)):
        data['day %i'%x]=y[x-1]
  
      
    # Creates padas DataFrame by passing  
    # Lists of dictionaries and row index. 
    df = pd.DataFrame(data, index =    [patient_ID]              )
      
    with open('document.csv','a') as fd:
        df.to_csv(fd, header=False)


patient_IDs= ['BKZI', 'MAMCZ', 'Anna Dzialak', 'ASCZ', 'BBZI', 'BMCZ'
             , 'DMCZ', 'EKZI', 'ELCZ', 'HKZI','JKCZ', 'JRCZ', 'JSCZ' , 'KKZI', 
             'MBCZ', 'MMCZ', 'MPCZ', 'RKZI', 'SBZI' , 'UNZI', 'ZPZI']


for i in patient_IDs:    
    data_processing(i)





