import pandas as pd
import matplotlib.pyplot as plt


def analysis():
    df = pd.read_csv('../data_clean/clean_data.csv')
    print(df)


analysis()
