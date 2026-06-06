# ================================
# COVID-19 Data Analysis Project
# Day 1 - Data Loading & First Look
# ================================

import pandas as pd

# Dataset load karo
df = pd.read_csv(r'C:\Users\HP\Desktop\covid19-data-analysis\data\owid-covid-data.csv')

# Basic information dekho
print("Dataset Shape (rows, columns):")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nKitne Countries hain:")
print(df['location'].nunique())

print("\nDate Range:")
print("Start:", df['date'].min())
print("End:  ", df['date'].max())


# ================================
# Day 2 - Data Cleaning
# ================================

# Sirf important columns select karo
columns_needed = ['location', 'date', 'total_cases', 'new_cases',
                  'total_deaths', 'new_deaths', 'total_vaccinations',
                  'people_vaccinated', 'population', 'continent']

df = df[columns_needed]

print("Selected Columns Shape:")
print(df.shape)

# Missing values check karo
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Duplicate rows check karo
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Date column ko datetime format mein convert karo
df['date'] = pd.to_datetime(df['date'])

print("\nDate Column Type:")
print(df['date'].dtype)

# Missing values fill karo
df['total_cases'] = df['total_cases'].fillna(0)
df['total_deaths'] = df['total_deaths'].fillna(0)
df['new_cases'] = df['new_cases'].fillna(0)
df['new_deaths'] = df['new_deaths'].fillna(0)
df['total_vaccinations'] = df['total_vaccinations'].fillna(0)

print("\nAfter Cleaning - Missing Values:")
print(df.isnull().sum())

print("\nData Cleaning Complete!")