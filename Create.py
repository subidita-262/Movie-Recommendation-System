import pandas as pd
import numpy as np

# reading the data from the preprocessed .csv file
df = pd.read_csv('df.csv')

#Update the dataset
def Correction(item):
    lst = str(item).split()
    if lst[-1] in ['the', 'a', 'an']:
        last_item = lst.pop()
        new_item = last_item + " " + " ".join(lst)
        new = new_item[:-1]
        return(new)
        
    else:
        return(item)
 

df["title"].apply(Correction)


title_lst = []
for i in list(df['title']):
    item = Correction(i)
    title_lst.append(item)

#Create new dataframe 
updated_data = pd.DataFrame({'col':title_lst})    
    

df['title'] = updated_data['col'] 

df.to_csv('Updated_df')

user_ratings = df.pivot_table(index = 'user_id', columns = 'title', values = 'rating')
user_ratings.head()

#Removing the movies which have less than 10 users who rated it and fill the NaN values with '0'
user_ratings = user_ratings.dropna(thresh = 10, axis = 1).fillna(0)
user_ratings.head()


item_similarity_df = user_ratings.corr(method = 'pearson')
item_similarity_df.head(50)

item_similarity_df.to_csv('item_similarity_df.csv')
