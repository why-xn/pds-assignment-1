import pandas as pd


def cleanup():
    df = pd.read_csv('../data_raw/raw_data.csv')

    # nothing to cleanup
    df.to_csv('../data_clean/clean_data.csv')


cleanup()
