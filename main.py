# importing the libraries
import pandas as pd

# read in the two Excel sheets as dataframes
df1 = pd.read_excel("File1.xlsx")
df2 = pd.read_excel("File2.xlsx")

# create an empty list to store the missing records
missing_records = []

# loop through each row in df1
for index, row in df1.iterrows():
    # check if the row exists in df2
    if not df2[df2['Serial Number'] == row['Serial Number']].empty:
        continue
    # if the row is not in df2, add it to the missing_records list
    missing_records.append(row)

# create a new dataframe from the missing_records list
missing_records_df = pd.DataFrame(missing_records)

# output the missing records to a new Excel sheet
missing_records_df.to_excel("missing_records.xlsx", index=False)
