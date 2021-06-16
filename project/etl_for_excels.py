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
                if file.find("combined") > - 1:
                    continue
                flat_files.append(f'{dir}{os.sep}{file}')
    return flat_files

def read_xlsx_to_df(file):
    file_name_with_extension = file.split(sep='\\')[-1]
    file_name = left(file_name_with_extension, len(file_name_with_extension) - 5)
    xlsx = pd.ExcelFile(file)
    df = pd.read_excel(xlsx, 'Closed items')
    print(file_name)
    print(df.shape[0])
    df['tracker_name'] = file_name
    return df

def main():

    # extract
    files = get_flat_files()
    dfs = [read_xlsx_to_df(file) for file in files]

    # transform
    combined = pd.concat(dfs)
    combined['Group Company'] = combined['Group Company'].map(lambda x: 'LHT' if x in ['LGB', 'LGM', 'LGE'] else x)
    combined.loc[(combined['Detailed Status'] == '5 - PO - sent to supplier') & (combined['Banf quality'].isnull()), 'Banf quality'] = 'not evaluated'
    combined.loc[(combined['Detailed Status'] == '7 - PR - rerouted') & (combined['Banf quality'].isnull()), 'Banf quality'] = 'rerouted'
    combined['PR nr'] = combined['PR nr'].astype(str)

    # load
    combined.to_excel('combined.xlsx', index=False)

if __name__ == "__main__":
    main()
