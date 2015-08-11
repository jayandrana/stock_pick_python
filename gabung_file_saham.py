import numpy as np
import pandas as pd
from datetime import datetime
from pandas.tseries.offsets import CustomBusinessDay
from pandas.tseries.offsets import Timestamp
from pandas.tseries.offsets import BDay
import matplotlib.pyplot as plt

#read listkode saham
def read_listkode( str ):
       fh = open(str)
       listkode = []
       for line in fh.readlines():
             listkode.append( line )

       fh.close()
       #print listkode
       return;

#calculate mean
def calculate_mean( str ):
        data = pd.read_csv(str)
        dataMean = data.mean(axis = 0 )
        return dataMean;


#fungsi gabung file csv
def gabung_csv():
        fh = open('listkode.txt')
        stockdataFrame = pd.DataFrame()
        list_ = []
        for kode in fh.readlines():
            str = 'try'+kode+'.csv'
            str2 = str.replace("\n","")
            try:
                data = pd.read_csv(str2)
                frame2 = pd.DataFrame(data, columns=['Kode','Date','Open','High','Low','Close','Volume','Adj Close'])
                frame2['Kode'] = kode.replace("\n","")
                list_.append(frame2)
            except ValueError:
                print "Oops!  That was no valid code.  Skip..."
        stockdataFrame = pd.concat(list_)
        stockdataFrame.to_csv("file_saham_gabung.csv")
        print "saved to file_saham_gabung.csv"
        fh.close()
def sort_indicators():
    data = pd.read_csv("file_saham_gabung.csv")
    dataMean = data.Close.mean(axis = 0)
    dataMean_ADRO =  data[data['Kode'] == 'ADRO'].Close.mean(axis = 0)
    dataMean_GROUP_by_Kode = data.groupby('Kode').Close.mean()
    print dataMean_GROUP_by_Kode.sort()
    
#fungsi utama
frameDate = pd.read_csv("frameDate.csv")
data = pd.read_csv("file_saham_gabung.csv")
frameMerge = pd.merge(frameDate,data[data['Kode']== 'AALI'],how='outer')  

print frameDate

print frameMerge


#create time stamp yyyy-mm-dd


