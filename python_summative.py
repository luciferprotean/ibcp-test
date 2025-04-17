import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import streamlit as st

df = pd.read_csv('athlete_events.csv')
df_gold = df[df['Medal'] == 'Gold']
print(df_gold.head())
athlete_counts = df_gold['Team'].value_counts()
print(athlete_counts)
athlete_counts_df = df_gold['Team'].value_counts().reset_index()
athlete_counts_df.columns = ['Team', 'Count']
print(athlete_counts_df.head())
top_10_countries = athlete_counts.head(20)
print(top_10_countries)
max_country = athlete_counts.idxmax()
print(max_country)
st.write("""
#IBCP Capstone
#Test deployment
Checking *italics* and line writes
""")
st.line_chart(athlete_counts_df, x="Team", y="Count")

