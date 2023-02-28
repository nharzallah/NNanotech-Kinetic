import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os
from itertools import islice

#Create directory to house all outputs
folder_name=input("What would you like to name the folder? ")
os.mkdir('./'+(folder_name)+'')

#Blocking pandas error of modifying original data
pd.options.mode.chained_assignment = None

#Convert Excel Sheets (Kinetics and Fold Change) into individual CSV Files for each Tissue Sample
os.mkdir('./Kinetics')
excel_file=input("Enter name of Excel File ")
f=input("index of first Kinetics sheet ")
l=input("index of last Kinetics sheet ")
sheets_dict=pd.read_excel(excel_file, sheet_name=None)
for name,sheet in islice(sheets_dict.items(),int(f),int(l)+1):
    sheet.to_csv(os.path.join('./Kinetics', name + '.csv'), index= None, header =False)

os.mkdir('./FC')
f=input("index of first FC sheet ")
l=input("index of last FC sheet ")    
for name,sheet in islice(sheets_dict.items(),int(f),int(l)+1):
    sheet.to_csv(os.path.join('./FC', name + '.csv'), index= None, header =False)

#Calculating Linear Regression slope (cleavage rate) for each tissue
os.mkdir('./Rate')

a = input("Do you want to use the same number of time points for all tissues? (y/n) ")
if a == "y":
    t=input("How many time points are you considering? ")

for filename in os.scandir('./Kinetics'):
    if(filename.path.endswith("csv")):
        name = os.path.splitext(os.path.basename(filename))[0]
        data=pd.read_csv(filename, header=None)
        av=np.zeros(shape=(len(data),int((len(data.columns)+1)/2)), dtype=object)

        j=0
        for i in range(int((len(data.columns)+1)/2)):
            av[0][i]=data[j][0]
            j=j+2
        for i in range(len(data)):
            av[i][0]=data[0][i]


        for i in range(1, len(av) ):
            k=1
            for j in range(1, len(av[0])):
                av[i][j]=(pd.to_numeric(data[k][i]) + (pd.to_numeric(data[k+1][i])))/2
                k=k+2
        
        average = pd.DataFrame(av)
        
        header=average.iloc[0]
        average=average[1:]
        average.columns=header
        average = average.apply(pd.to_numeric)
        
        #ask for number of time points
        if a == "n":
            t=input("How many time points are you considering for " + name + "? ")
            average=average[:int(t)]
        else:
            average=average[:int(t)]


        x=np.array(average['Time (min)']).reshape(-1,1)
        rate=average.iloc[:1, :]
        
        rate.iloc[0,0] = name
        rate.columns.values[0]= t +' Time Points'

        for i in range(1,average.shape[1]):
            y=np.array(average.iloc[:,i]).reshape(-1,1)
            regressor=LinearRegression()
            regressor.fit(x,y)
            rate.iloc[0,i]=float(regressor.coef_)
            
        rate.to_csv(os.path.join('./Rate/', name + '_Rate.csv'))


#Combining Cleavage Rates for all tissues in one file
import glob
os.chdir('./Rate/')
extension='csv'
all_filenames=[i for i in glob.glob('*.{}'.format(extension))]
combined_csv=pd.concat([pd.read_csv(f, index_col=0) for f in all_filenames])
combined_csv.to_csv("Rates.csv", index=False)

#Converting the Cleavage rate into PRISM friendly format
data=pd.read_csv("Rates.csv",  index_col=0, header=None)
data=data.transpose()
data.to_csv('Rates.csv', index=False)


os.mkdir('../PRISM')
os.system('cd ..; osascript PRISM-Apple-Launcher.scpt; mv Kinetics Rate PRISM FC '+(folder_name)+'')
