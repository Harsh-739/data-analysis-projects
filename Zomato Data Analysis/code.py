import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/Users/harshpreet/Desktop/data-analysis-projects/Zomato Data Analysis/Zomato-data-.csv')
#print(df.head())

# 1. Converting the rate column to a float by removing denominator characters
def handleRate(value):
    value=str(value).split('/')
    value=value[0]
    return float(value)

df['rate']=df['rate'].apply(handleRate)
print(df.head())

# 2. Summary of the dataframe
print(df.info())

# 3. Chaeking for missing or null values to identify any data gaps
print(df.isna().sum())

# 4. Exploring Restaurant  types-identify popular restaurant categories
print(df.columns)
print(df['listed_in(type)'].value_counts())
sns.countplot(x=df['listed_in(type)'], palette='Set2')
plt.title('Restaurnat by categories')
plt.show()


# 5. Votes by Restaurant type - count of votes for each categories
grouped_data=df.groupby('listed_in(type)')['votes'].sum()
result=pd.DataFrame({'votes':grouped_data})
plt.plot(result, c='green', marker='o')
plt.xlabel('Type of Restaurant')
plt.ylabel('Votes')
plt.show()


# 6. Find the restaurant with the highest number of votes many restaurant accept online orders
print(df.columns)
max_votes=df['votes'].max()
restaurant_with_max_votes=df.loc[df['votes']==max_votes,'name']
print("Restaurant with maximum votes: ")
print(restaurant_with_max_votes)



# 7. Explore the online_column to see how many restaurants accept online orders
sns.countplot(x=df['online_order'])
plt.show()

# 8. Distribbution of rating from the rate column
plt.hist(df['rate'], bins=5)
plt.title('Rating Distribution')
plt.show()

# 9. Analyse the "approx_cost(for two people)" column to find the preferred price range
couple_data=df['approx_cost(for two people)']
sns.countplot(x=couple_data)
plt.show()

# 10. Compare rating between restaurants that accept online orders and those that don't
plt.figure(figsize=(6,6))
sns.boxplot(x='online_order', y='rate', data=df)
plt.show()


# 11. How many restaurant of each type allow / do not allow online orders(Relationship)
pivot_table=df.pivot_table(
            index='listed_in(type)',
            columns='online_order',
            aggfunc='size',
            fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Heatmap')
plt.xlabel('Online orders')
plt.ylabel('Listed in types')
plt.show()