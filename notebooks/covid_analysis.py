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