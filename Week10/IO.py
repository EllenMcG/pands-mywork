# IO.py
# This program uses inbuilt functions completed within a list 
# of data

# Author Ellen McGrory

import pandas as pd

list_data = [
    ['John', 'math', 23],
    ['John', 'programming', 66],
    ['Mary', 'math', 45],
    ['May', 'programming', 33],
    ['Mark', 'STEM', 57],
    ['Mark', 'programming', 70],
    ['Mark', 'math', 73],
    ['John', 'programming', 61]
]

# Converting list to dataframe
df = pd.DataFrame(list_data,columns=['name','subject','grade'])
print(df.head(3))

# saving dataframe to .CSV file called 'grades.csv'
# There is a comma at the start of the first row, or the header
# row as the index does not have a header in csv file, but setting
# index=False within .to_csv() function will remove this 
# as the index is not passed from the dataframe 
path = '.data'
csv_filename = path + 'grades.csv'
df.to_csv(csv_filename)

# Writing dataframe (df) to Excel file called 'grades.xlsx' in sheet 'data
excel_filename = path + 'grades.xlsx'
df.to_excel(excel_filename, index=False, sheet_name='data')

# Adding a descrption of the 'grades.xlsx' file to another sheet called
# 'summary' using the .describe() method 

with pd.ExcelWriter(excel_filename, engine='openpyxl', mode='a') as writer:
    df.describe().to_excel(writer, sheet_name='summary')

# Mean of grade
mean = df['grade'].mean()
print(mean)


