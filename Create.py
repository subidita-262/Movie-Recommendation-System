import pandas as pd
import numpy as np

# reading the data from the preprocessed .csv file
df = pd.read_csv('df.csv')

user_ratings = df.pivot_table(index = 'user_id', columns = 'title', values = 'rating')
user_ratings.head()

#Removing the movies which have less than 10 users who rated it and fill the NaN values with '0'
user_ratings = user_ratings.dropna(thresh = 10, axis = 1).fillna(0)
user_ratings.head()


item_similarity_df = user_ratings.corr(method = 'pearson')
item_similarity_df.head(50)

item_similarity_df.to_csv('item_similarity_df.csv')