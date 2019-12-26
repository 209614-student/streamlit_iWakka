import email
import getpass
import imaplib
import os
import sys
import pandas as pd
import streamlit as st
import numpy as np


file_list = []

def download_dataraw():
    userName = 'sterowanierobotow2@gmail.com'
    passwd = 'IloveiWakka!!!'

    try:
        imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
        typ, accountDetails = imapSession.login(userName, passwd)
        if typ != 'OK':
            st.write('Not able to sign in!')
            raise

        imapSession.select('Inbox')
        typ, data = imapSession.search(None, 'ALL')
        if typ != 'OK':
            st.write('Error searching Inbox.')
            raise
        
        for msgId in data[0].split():
            typ, messageParts = imapSession.fetch(msgId, '(RFC822)')

            emailBody = messageParts[0][1]
            mail = email.message_from_bytes(emailBody)
            subject = mail['subject']
            if subject.find('tch') > -1:
                for part in mail.walk():
                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get('Content-Disposition') is None:
                        continue

                    fileName = part.get_filename()
                    global life_list
                    file_list.append(fileName)
                    
                    print (fileName)
                    st.write(fileName)
        print ('Done')

    
    except :
        print ('Not able to download all attachments.')
        
        return file_list

    
    
def data_processing(patient_ID, file_list):

    CODE_SHEET = pd.read_csv('code_ocena_12.csv')
    # find excel files in directry whose name is from the argument(subject)
    def find_data(patient_ID, file_list):   

        res = list(filter(lambda x: patient_ID in x, file_list)) 

    # printing result  
#        print ("All strings with given substring are : " + str(res))

        result_sheets = []
        for file_path in file_list:
            if  file_path.find(str(patient_ID)) > -1: 
                result_sheet = pd.read_csv(file_path )
                result_sheets.append(result_sheet )


        return result_sheets

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

    y=[]
    Y1=[]
    def nwm():
        result_scheets = find_data(patient_ID, file_list)
        for i in result_scheets:
            a=computed(i)['Total']
            a=np.round(a,3)
            y.append(a)
            Y1=[i for i in range(1,(len(y)+1))]  

        data = dict()
        for x in range(1,len(y)):
            data['day %i'%x]=y[x-1]


        # Creates padas DataFrame by passing  
        # Lists of dictionaries and row index. 
        df = pd.DataFrame(data, index =    [patient_ID]              )
        return df

    df = nwm()
    return df

def download_data():

    st.header(" It's actually first step to start process data of your patient.")
    st.header(" Just follow the instruction!")
    st.markdown("Hi! It's fisrt step! Just click the bottom below and download data!")
    button =st.button('START DOWNLOAD DATA')
    if button:
       download_dataraw() 
    st.write ('Atfter downloading data, you can press the button below to start processing them!')
    add=st.text_input('dodaj ID')
    
    patient_ID = ['BKZI','ZPZI','HKZI','BBZI','SBZI','DMCZ','JRCZ','JKCZ']
    patient_ID.append(add)
    option = st.selectbox(
            'Which patient would you like to choose?',patient_ID
    )
    for i in patient_ID:
        if option == i:
            patient_ID = i
            button2 = st.button('START PROCESSING DATA')
            if button2:
                data_processing(patient_ID,file_list)

