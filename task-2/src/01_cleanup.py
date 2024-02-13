import pandas as pd


def find_grade(n):
    if n >= 93:
        return 'A'
    elif n >= 90:
        return 'A-'
    elif n >= 87:
        return 'B+'
    elif n >= 83:
        return 'B'
    elif n >= 80:
        return 'B-'
    elif n >= 77:
        return 'C+'
    elif n >= 73:
        return 'C'
    elif n >= 70:
        return 'C-'
    elif n >= 67:
        return 'D+'
    elif n >= 63:
        return 'D'
    elif n >= 60:
        return 'D-'
    else:
        return 'F'


def cleanup():
    df = pd.read_csv('../data_raw/StudentsPerformance.csv')
    math_grade = []
    reading_grade = []
    writing_grade = []

    # generating grades of the subjects based on the score
    for index, row in df.iterrows():
        math_grade.append(find_grade(df.at[index, 'math score']))
        reading_grade.append(find_grade(df.at[index, 'reading score']))
        writing_grade.append(find_grade(df.at[index, 'writing score']))

    df['math grade'] = math_grade
    df['reading grade'] = reading_grade
    df['writing grade'] = writing_grade

    df.to_csv('../data_clean/clean_data.csv')


cleanup()
