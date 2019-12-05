import pandas as pd
file1=pd.read_csv("hypertension.csv")
file2=pd.read_csv("essential.csv")
Data = pd.concat([file1,file2]).drop_duplicates('ID', keep=False) #remove duplicates except for first occurence
Data.to_csv('output.csv', index=False) #Export data to new csv file
