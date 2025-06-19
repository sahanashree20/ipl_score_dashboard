import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Config
st.set_page_config(page_title="IPL Dashboard", layout="wide")

# Connect to database
conn = sqlite3.connect("ipl_data.db")
matches = pd.read_sql("SELECT * FROM matches", conn)
deliveries = pd.read_sql("SELECT * FROM deliveries", conn)

# Sidebar
st.sidebar.title("🏏 IPL Filters")
selected_team = st.sidebar.selectbox("Select Team", sorted(matches['team1'].unique()))

# Filtered matches
team_matches = matches[(matches['team1'] == selected_team) | (matches['team2'] == selected_team)]

# Title
st.title(f"📊 IPL Dashboard for {selected_team}")

# Stats
st.metric("Total Matches", len(team_matches))
st.metric("Wins", matches[matches['winner'] == selected_team].shape[0])
st.metric("Toss Wins", matches[matches['toss_winner'] == selected_team].shape[0])

# Match table
st.subheader("Recent Matches")
st.dataframe(team_matches.tail(10))

# Pie chart of wins per team
st.subheader("Wins by All Teams")
fig, ax = plt.subplots()
matches['winner'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
ax.set_ylabel("")
st.pyplot(fig)

conn.close()
