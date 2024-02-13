import pandas as pd


def cleanup():
    df = pd.read_csv('../data_raw/raw_data.csv')

    # changing data type of Frailty to integer
    for index, row in df.iterrows():
        if df.at[index, 'Frailty'] == 'Y':
            df.at[index, 'Frailty'] = 1
        else:
            df.at[index, 'Frailty'] = 0

    df.to_csv('../data_clean/clean_data.csv')


cleanup()
