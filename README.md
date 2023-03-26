# Comparing-excel-sheets-for-missing-records
This Python code uses the Pandas library to compare two Excel sheets(containing common serial numbers in records) and identify missing records in one of them.

The first two lines of code read in the two Excel sheets as dataframes using the Pandas read_excel() function.

The next few lines of code create an empty list called missing_records, which will be used to store the missing records from the first Excel sheet.

The for loop iterates through each row in the first dataframe (df1) using the iterrows() function. For each row, the code checks if it exists in the second dataframe (df2) by using the Pandas empty function. If the row exists in df2, the code skips to the next row. If the row is not in df2, the code appends it to the missing_records list.

After the for loop completes, the code creates a new dataframe (missing_records_df) from the missing_records list. Finally, the code outputs the missing records to a new Excel sheet called "missing_records.xlsx" using the Pandas to_excel() function.

This code identifies the missing records in the first Excel sheet that do not exist in the second Excel sheet and outputs them to a new Excel sheet.
