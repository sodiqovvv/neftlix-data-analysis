import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_excel("netflix_titles.xlsx")

# print(df.shape)  # Allows us to know the number of rows and columns

# print(df.isnull().sum())  # finding missing values

# print(df.duplicated().sum())  # shows sum of all duplicate values
# df.drop_duplicates()  # if found any, remove

# df.fillna({'director': "Unknown"}, inplace=True)
# df.fillna({'cast': "Unknown"}, inplace=True)
# df.fillna({'country': "Unknown"}, inplace=True)
# df.to_csv("processed_data.csv", index=False)  # cleaning and creating file with fresh data

df = pd.read_csv("processed_data.csv")

# print(df.value_counts("type"))  # shows how many movies and tv shows

# df['release_year'].value_counts().sort_index().plot(kind='bar', figsize=(15,5))
# plt.show() # displays movie release numbers

# print(df['rating'].value_counts())  # most used rating

# print(df['listed_in'].value_counts())  # most used genres

# print(df[df['listed_in'] != 'Unknown']['listed_in'].str.split(', ').explode().unique())  # shows all the unique genres


































































