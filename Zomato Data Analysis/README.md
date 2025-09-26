Zomato Data Analysis
This project analyzes a dataset of 148 restaurants to explore trends in restaurant categories, online ordering, ratings, and pricing.

Dataset Overview
148 rows, 7 columns

Key columns:
name: Restaurant name
online_order: Accepts online orders (Yes/No)
votes: Number of votes
rate: Rating (converted to float)
approx_cost(for two people): Price for two
listed_in(type): Restaurant category

Libraries Used
pandas, numpy – Data manipulation
matplotlib, seaborn – Data visualization



Analysis Steps
Data Cleaning:
    Converted rate to float.       
Exploratory Data Analysis: 
    Checked for missing values and dataset info.
    Counted restaurants by category.
Votes Analysis:
    Total votes by restaurant type.
    Identified restaurant with maximum votes.
Online Ordering Analysis:
    Count of restaurants accepting online orders.
    Compared ratings for online vs offline restaurants.
Ratings & Cost Distribution:
    Histogram of restaurant ratings.
    Analysis of cost for two people.
Relationship Analysis:
    Pivot table and heatmap: restaurant type vs online ordering.

            
Visualizations
Countplot: Restaurants by category
Line plot: Total votes by type
Histogram: Rating distribution
Boxplot: Rating vs online ordering
Heatmap: Restaurant type vs online ordering
