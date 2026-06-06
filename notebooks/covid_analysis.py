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




# ================================
# Day 3 - EDA + Analysis
# ================================

# Continents wali rows hatao (sirf countries chahiye)
continents = ['World', 'Asia', 'Europe', 'Africa', 'North America',
              'South America', 'Oceania', 'European Union',
              'High income', 'Low income', 'Upper middle income',
              'Lower middle income']

df_countries = df[~df['location'].isin(continents)]

# India ka data check karo
india_data = df[df['location'] == 'India']
print("\nIndia Last Row:")
print(india_data.tail(1)[['location', 'total_cases', 'total_deaths']])

# Latest date ka data lo har country ka
# Last non-zero value lo har country ka
latest = df_countries[df_countries['total_cases'] > 0].groupby('location').last().reset_index()

# Top 10 most affected countries by total cases
top10_cases = latest.nlargest(10, 'total_cases')[['location', 'total_cases']]
print("Top 10 Countries by Total Cases:")
print(top10_cases)

# Top 10 countries by total deaths
top10_deaths = latest.nlargest(10, 'total_deaths')[['location', 'total_deaths']]
print("\nTop 10 Countries by Total Deaths:")
print(top10_deaths)

# Death rate calculate karo
latest['death_rate'] = (latest['total_deaths'] / latest['total_cases']) * 100
top10_death_rate = latest.nlargest(10, 'death_rate')[['location', 'death_rate']]
print("\nTop 10 Countries by Death Rate (%):")
print(top10_death_rate)

# India, USA, Brazil comparison
countries = ['India', 'United States', 'Brazil']
comparison = latest[latest['location'].isin(countries)][['location', 'total_cases', 'total_deaths']]
print("\nIndia vs USA vs Brazil:")
print(comparison)