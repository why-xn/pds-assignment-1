import pandas as pd
import matplotlib.pyplot as plt


def analysis():
    df = pd.read_csv('../data_clean/clean_data.csv')

    # Plotting a scatter plot with Profit represented by marker colors
    plt.scatter(df['Age'], df['Grip Strength'], c=df['Frailty'], cmap='viridis', s=100, alpha=0.5)
    plt.colorbar(label='Frailty')  # Add color bar indicating Profit values
    plt.title('Sales Over Years (Scatter Plot)')
    plt.xlabel('Age (Years)')
    plt.ylabel('Grip Strength (Kg)')
    plt.grid(True)
    plt.show()
    plt.savefig('../result/frailty_based_on_age_and_grip_strength.png', format='png', dpi=300)


analysis()
