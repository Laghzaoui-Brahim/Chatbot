from operator import index
from grpc import Status
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

def getLinkActivitie(num):
    link = 'Numero du lien n\'est pas correcte'
    if num == 1 :
        link = '<a href="https://docs.google.com/document/d/1BgfvIXofvE4HaXtuT7S40bKaAfsRCuDf/edit?usp=sharing&ouid=101457582345898735112&rtpof=true&sd=true" target="_blank">SecWF</a>' 
    if num == 2 :
        link = '<a href="https://docs.google.com/document/d/1hz1xJal5ILCl1vboNzPNThBla0eLAkm2/edit?usp=sharing&ouid=101457582345898735112&rtpof=true&sd=true" target="_blank">MP</a>'
    if num == 3 :
        link = '<a href="https://docs.google.com/document/d/1qWjLoEYVC0bJze7KSNe7zjlvdBNCM7IZ/edit?usp=sharing&ouid=101457582345898735112&rtpof=true&sd=true" target="_blank">Section Dispatch</a>'
    if  num == 4 :
        link = '<a href="https://drive.google.com/file/d/1lDP-sYLcKb0-b83urAdSPgw9ys3xKEbn/view?usp=sharing"></a>'
    if num == 5 :
        link = '<a href="https://docs.google.com/document/d/1SQur2aveYLYlG-D35ZU5o1Z1DXgAHk1H/edit?usp=sharing&ouid=101457582345898735112&rtpof=true&sd=true" target="_blank">Primary SecWF</a>'
    if num == 6 :
        link ='<a href="https://drive.google.com/file/d/1OozrrkW6Nzaacuw6hfsPdJCR9wz84Q7w/view" target="_blank">Section Dispatch</a>'
    
    return link

    
"""Email : accessgoogleapi@airbusproject.iam.gserviceaccount.com"""

def getSheet(File,Sheet):
    scopes =['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('secret_key.json',scopes=scopes)
    file = gspread.authorize(creds)
    workbook = file.open(File)
    sheet = workbook.worksheet(Sheet)
    data = sheet.get_all_values()
    df = pd.DataFrame(data[4:],columns=data[3])
    return df

def getItem(df,AM):
    ind = 0
    for i in df.loc[:,"AM\n BDP\n LR\n number"]:
        if i == str(AM) :
            return df.loc[ind]
        ind = ind + 1  

def getStatus(row):
    dic = {'Message' : 'Your request is taken into consideration','status' : row['Status'],'Flow': row['Flow']}
    m = 0
    if(str.lower(row['Supplier']) == 'inhouse'):
        m = 'FAUF'
    else :
        m = 'PO'
    if(row['Status'] == 'New item') :
        return dic
        
    dic[m] = row[m]
    if (row['Status'] == 'to be checked') :        
        dic['Message'] = 'your request is being processed'
        dic[m] = row[m]
        return dic
    if (row['Status'] == 'ordered') :
        dic['Message'] = 'Your request is being processed'
        dic[m] = row[m]
        dic['deadline ODD TLS'] = row['deadline -\n ODD TLS']
        return dic
    
    dic['Delivery Note Number'] = row['Delivery \n Note \n Number']
    dic['QTY'] = row['QTY']
    dic['Prep.'] = row['Prep.']

    if (row['Status'] == 'Shipping in progress') :
        dic['Message'] = 'Your request is being sent'
        return dic

    if(row['Status'] == 'Shipped') :
        dic['Message'] = 'Your request is sent'

    if(row['Status'] == 'Delivered'):
        dic['Message'] = 'Your request is delivered'
    
    dic['Shipped date HAM'] = row['Shipped \n date \n HAM']
    
    return dic

  
def getFile(AM):
    files = ['A330 TLS CABIN- Secondary Flow',
            'TLS_A330_Blocking point MP - PODA3 (Potential)',
            'A330 TLS GREEN- Bons_Refus_2022 (Secondary Flow)']
    for file in files :
        df = getSheet(file,'Feuille 1')
        for i in df.loc[:,"AM\n BDP\n LR\n number"]:
            if i == str(AM) :
                return file
    return 'None'


def main(AM) :
    file = getFile(AM)
    Result = str()
    try :
        print(file)
        data = getSheet(file,'Feuille 1')
        row = getItem(data,AM)
        dic = getStatus(row)
        for cle, value in dic.items() :
            Result +=  '<br>' + '-' + str(cle) + ' : ' + str(value) 
    except Exception as exp:
        print(exp)
        Result = "Your request not available"
        
    return Result

