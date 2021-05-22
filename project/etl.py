import os
import pyodbc
import pandas as pd

path = os.getcwd()
conn_str = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=.\transactions.accdb;'
table_name = 'tblMain'

def initilize_db_conn():
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    return conn, cursor

def format_dataframe_rows_as_list_of_tuples(df):
    df = df.fillna('')
    rows = [tuple(cell) for cell in df.values]
    return rows

def get_flat_files():
    flat_files = []
    for dir, subdirs, files in os.walk(path):
        for file in files:
            if file.endswith(".csv"):
                flat_files.append(f'{dir}{os.sep}{file}')
    return flat_files

def read_csv_to_df(file):
    cols = list(pd.read_csv(file, nrows =1))
    df = pd.read_csv(file, usecols = [col for col in cols if col not in ['id', 'deleted', 'last_update', 'time', 'payer_name']], encoding = "latin1")
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
    combined['verified'] = combined['verified'].map(lambda x: str(x))

    # load
    conn, cursor = initilize_db_conn()
    sql_str = '''INSERT INTO tblMain(id, amount, curr, verified, country, city, alert) VALUES(?,?,?,?,?,?,?)'''
    rows = format_dataframe_rows_as_list_of_tuples(combined)

    for row in rows:
        cursor.execute(sql_str, row)

    conn.commit()

if  __name__ == '__main__':
    main()
