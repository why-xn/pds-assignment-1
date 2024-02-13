import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import seaborn as sns


# Graph 1 is console printed
def graph1(df):
    grouped_df = df.groupby(['race/ethnicity', 'gender']).size().unstack()
    table_chart = tabulate(grouped_df, headers='keys', tablefmt='grid')
    print("Number of Students based on Race/Ethnicity and Gender")
    print(table_chart)


# Grades in different subjects based on Gender
def graph2(df):
    math_df = df[['gender', 'math grade']]

    reading_df = df[['gender', 'reading grade']]

    writing_df = df[['gender', 'writing grade']]

    # Grouping and unstacking for each subject
    math_grouped_df = math_df.groupby(['gender', 'math grade']).size().unstack()
    reading_grouped_df = reading_df.groupby(['gender', 'reading grade']).size().unstack()
    writing_grouped_df = writing_df.groupby(['gender', 'writing grade']).size().unstack()

    # Plotting the bar charts
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(8, 12))

    math_grouped_df.plot(kind='bar', ax=axes[0], rot=0)
    axes[0].set_title('Math Grades By Gender')
    axes[0].set_xlabel('Gender')
    axes[0].set_ylabel('Number of Students')
    axes[0].legend(title='Grades')

    reading_grouped_df.plot(kind='bar', ax=axes[1], rot=0)
    axes[1].set_title('Reading Grades By Gender')
    axes[1].set_xlabel('Gender')
    axes[1].set_ylabel('Number of Students')
    axes[1].legend(title='Grades')

    writing_grouped_df.plot(kind='bar', ax=axes[2], rot=0)
    axes[2].set_title('Writing Grades By Gender')
    axes[2].set_xlabel('Gender')
    axes[2].set_ylabel('Number of Students')
    axes[2].legend(title='Grades')

    plt.tight_layout()
    plt.savefig('../result/grades_based_on_genders.png', format='png', dpi=300)


# Grades in different subjects based on Education Level of Parents
def graph3(df):
    math_df = df[['parental level of education', 'math grade']]

    reading_df = df[['parental level of education', 'reading grade']]

    writing_df = df[['parental level of education', 'writing grade']]

    # Grouping and unstacking for each subject
    math_grouped_df = math_df.groupby(['parental level of education', 'math grade']).size().unstack()
    reading_grouped_df = reading_df.groupby(['parental level of education', 'reading grade']).size().unstack()
    writing_grouped_df = writing_df.groupby(['parental level of education', 'writing grade']).size().unstack()

    # Plotting the bar charts
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(8, 12))

    math_grouped_df.plot(kind='bar', ax=axes[0], rot=0)
    axes[0].set_title('Math Grades By Parental Level of Education')
    axes[0].set_xlabel('Gender')
    axes[0].set_ylabel('Number of Students')
    axes[0].legend(title='Grades')

    reading_grouped_df.plot(kind='bar', ax=axes[1], rot=0)
    axes[1].set_title('Reading Grades By Parental Level of Education')
    axes[1].set_xlabel('Gender')
    axes[1].set_ylabel('Number of Students')
    axes[1].legend(title='Grades')

    writing_grouped_df.plot(kind='bar', ax=axes[2], rot=0)
    axes[2].set_title('Writing Grades By Parental Level of Education')
    axes[2].set_xlabel('Gender')
    axes[2].set_ylabel('Number of Students')
    axes[2].legend(title='Grades')

    plt.tight_layout()
    plt.savefig('../result/grades_based_on_parental_level_of_education.png', format='png', dpi=300)


# Distribution of lunch types
def graph4(df):
    lunch_counts = df['lunch'].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(lunch_counts, labels=lunch_counts.index, autopct='%1.1f%%', colors=['green', 'red'])
    plt.title('Pie Chart of Lunch Types')
    plt.savefig('../result/pie_chart_of_lunch_types.png', format='png', dpi=300)


# Reading vs Writing Scores
def graph5(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='reading score', y='writing score', data=df, hue='gender', palette='Set1', alpha=0.7)
    plt.xlabel('Reading Score')
    plt.ylabel('Writing Score')
    plt.title('Scatter Plot of Reading vs. Writing Scores')
    plt.grid(True)
    plt.legend(title='Gender')
    plt.savefig('../result/scatter_plot_of_reading_vs_writing.png', format='png', dpi=300)


def analysis():
    df = pd.read_csv('../data_clean/clean_data.csv')
    graph1(df)
    graph2(df)
    graph3(df)
    graph4(df)
    graph5(df)

    print("All Charts are saved in result folder")



analysis()
