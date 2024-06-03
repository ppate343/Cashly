import pandas as pd 
import numpy as np


df = pd.read_csv('all_leds.csv')

#creating new column middle name
df.insert(loc=3, column='Middle Name', value=['' for i in range(df.shape[0])])

# Convert all entries to strings and replace NaN with empty strings
df['First Name'] = df['First Name'].astype(str).replace('nan', '')

df['Last Name'] = df['Last Name'].astype(str).replace('nan', '')

# Updated function to split the names
def split_name(name, middle_name, last_name):

    parts = last_name.split()
    parts_name = name.split()
    #last_name_parts = last_name.split()

    #1. check if name and last name exist
    if name and last_name:
        #if middle name exists in first name return it
        if len(parts) ==2: 
            return parts[0], '', parts[1]
        elif len(parts_name) ==2: 
            #else return empty string for middle name
            return parts_name[0], '', parts_name[1]
        else: 
            return name, '', last_name

    if name and last_name =='': 
        if len(parts_name) ==1: 
            return name, '', name
 
        elif len(parts_name) ==2:
            return parts[0], '', parts[1]

        elif len(parts_name) ==3: 
            return parts_name[0], parts_name[1], parts_name[2]

    if name=='' and last_name: 
        if len(parts) ==1: 
            return last_name, '', last_name
     
        elif len(parts) ==2:
            return parts[0], '', parts[1]
    
        elif len(parts) ==3: 
            return parts[0], parts[1], parts[2]

# Apply the updated split_name function to the DataFrame
df[['First Name', 'Middle Name', 'Last Name']] = df.apply(
    lambda row: pd.Series(split_name(row['First Name'], row['Middle Name'], row['Last Name'])),
    axis=1
)


# loop through to capitalize first letter 
def capitalize_first_letter(s):
    #check if attr is string 
    return s[0].upper() + s[1:] if isinstance(s, str) and s else s

# Capitalizing the first letter in each of the name columns
df['First Name'] = df['First Name'].apply(capitalize_first_letter)
df['Middle Name'] = df['Middle Name'].apply(capitalize_first_letter)
df['Last Name'] = df['Last Name'].apply(capitalize_first_letter)


#defining chars to remove from phone number columns
char_remove = ['p:+', '+', '(', ')', ' ', '-']

# Function to clean the phone number
def clean_num(num):
    #check is num does not exist
    if pd.isna(num) or num is None:
        return num
    # replace chars to remove with empty space
    for char in char_remove:
        num = num.replace(char, '')
    # Add area code '1' if not included
    if not num.startswith('1'):
        num = '1' + num
    return num


df['Phone'] = df['Phone'].apply(clean_num)

#save to csv file 
df.to_csv('leads_clean.csv', index=False)