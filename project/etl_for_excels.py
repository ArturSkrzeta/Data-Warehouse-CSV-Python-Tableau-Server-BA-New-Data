import pandas as pd
import os
path = os.getcwd()

def left(s, amount):
    return s[:amount]

def get_flat_files():
    flat_files = []
    for dir, subdirs, files in os.walk(path):
        for file in files:
            if file.endswith(".xlsx"):
                flat_files.append(f'{dir}{os.sep}{file}')
    return flat_files

def read_xlsx_to_df(file):
    file_name_with_extension = file.split(sep='\\')[-1]
    file_name = left(file_name_with_extension, len(file_name_with_extension) - 5)
    xlsx = pd.ExcelFile(file)
    df = pd.read_excel(xlsx, 'Closed items')
    df['tracker_name'] = file_name
    return df

def main():

    files = get_flat_files()
    count = len(files)
    dfs = [read_xlsx_to_df(file) for file in files]
    combined = pd.concat(dfs)
    combined.to_csv('combined.csv', index=False)

if __name__ == "__main__":
    main()

# xls = pd.ExcelFile('path_to_file.xls')
# df1 = pd.read_excel(xls, 'Sheet1')
# df2 = pd.read_excel(xls, 'Sheet2')
