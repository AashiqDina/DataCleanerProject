import pandas as pd
import os 

files = os.listdir("Input")
if(len(files) != 0):
    for i in range(len(files)):
        if (files[i].lower().endswith('.csv')):
            DirtyFile = pd.read_csv("Input/" + files[i])
            print(DirtyFile.duplicated())
            print(DirtyFile.duplicated().sum())
            
else:
    print("There are no files in this folder")

