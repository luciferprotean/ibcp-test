import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

df = pd.read_csv('athlete_events.csv')
df_gold = df[df['Medal'] == 'Gold']
print(df_gold.head())
athlete_counts = df_gold['Team'].value_counts()
print(athlete_counts)
top_10_countries = athlete_counts.head(20)
print(top_10_countries)
max_country = athlete_counts.idxmax()
print(max_country)

