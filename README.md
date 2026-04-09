# trendpulse-kaustubh

TrendPulse: Live Trending Data Pipeline
TrendPulse is a Python-based data pipeline that fetches live trending stories from the HackerNews API, cleans the data, performs statistical analysis, and visualizes the insights. This project was built across 4 modular tasks.

🚀 Project Overview
The pipeline follows these four stages:

1) Data Collection: Fetches trending JSON data from HackerNews API.
2) Data Processing: Cleans the raw data and saves it as a CSV.
3) Data Analysis: Uses Pandas and NumPy to compute trends and engagement scores.
4) Data Visualization: Generates charts and a dashboard to visualize findings.

📁 Repository Structure

trendpulse-kaustubh

task1_data_collection.py  # Fetches raw JSON data
task2_data_processing.py  # Cleans data and exports to CSV
task3_analysis.py         # Performs statistical analysis
task4_visualization.py    # Generates PNG charts

data/                     # Stores JSON, analysed.csv and clean.csv files
trends_YYYYMMDD.json
trends_clean.csv
trends_analysed.csv

outputs/                  # Stores generated 3 charts and dashboard
chart1_top_stories.png
chart2_categories.png
chart3_scatter.png
dashboard.png
