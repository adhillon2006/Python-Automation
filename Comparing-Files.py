import os
import numpy as np
import pandas as pd

file_path = 'C:/Users/adhillon/Audit Files/Workday'
os.chdir(file_path)# directory

list_of_files= []

for file_names in os.listdir():
    list_of_files.append(os.path.join(file_path+'/'+ file_names))

file_path = 'C:/Users/adhillon/Audit Files/Tenant'
os.chdir(file_path)# directory

list_of_files2= []

for file_names in os.listdir():
    list_of_files2.append(os.path.join(file_path+'/'+ file_names))

df = pd.DataFrame(columns=['Path Name','Audit'])

for files in range(0,len(list_of_files2)):
    df= df.append({'Path Name': list_of_files[files],
               'Audit': pd.read_excel(list_of_files[files]).equals(pd.read_excel(list_of_files2[files]))},ignore_index=True)
