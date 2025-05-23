import pandas as pd
import os 

files = os.listdir("Input")
if(len(files) != 0):
    for i in range(len(files)):
        if (files[i].lower().endswith('.csv')):
            DirtyFile = pd.read_csv("Input/" + files[i])
            # Fix Emails
            DirtyFile['Email'] = DirtyFile['Email'].astype(str).str.lower() # Convert to lowercase
            DirtyFile = DirtyFile[(DirtyFile['Email'].str.count('@') == 1) & (DirtyFile['Email'].str.contains(r'\.'))] # Checks if the email has exactly 1 @ and contains at least 1 . (for the end part like .com or .co.uk)
            DirtyFile = DirtyFile.drop_duplicates(subset=['Email'], keep='first') # Removes any duplicate emails since emails should be unique

            # Fix Names
            DirtyFile['Name'] = DirtyFile['Name'].astype(str).str.lower() # Convert to lowercase
            DirtyFile['Name'] = DirtyFile['Name'].str.strip() # remove spaces at the front or back
            DirtyFile['Name'] = DirtyFile['Name'].str.replace(r'\s+', ' ', regex=True) # remove spaces between names (first and last names)
            print(DirtyFile)
            
else:
    print("There are no files in this folder")

