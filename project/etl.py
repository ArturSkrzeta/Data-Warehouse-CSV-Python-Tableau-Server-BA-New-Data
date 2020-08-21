import os
import pandas as pd
path = os.getcwd()

def get_flat_files():
    flat_files = []
    for dir, subdirs, files in os.walk(path):
        for file in files:
            if file.endswith(".csv"):
                flat_files.append(f'{dir}{os.sep}{file}')
    return flat_files

def read_csv_to_df(file):
    cols = list(pd.read_csv(file, nrows =1))
    df = pd.read_csv(file, usecols = [col for col in cols if col not in ['id', 'deleted', 'last_update','time']])
    return df

def main():

    # extract
    files = get_flat_files()
    count = len(files)
    dfs = [read_csv_to_df(file) for file in files]

    # transfrom
    combined = pd.concat(dfs)
    combined.reset_index(inplace=True, drop=True)
    combined['alert'] = combined['amount'].map(lambda x: 'Yes' if x < -9000 else 'No')

    # load
    combined.to_csv('data.csv')

if __name__ == '__main__':
    main()
