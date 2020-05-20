import numpy as np
import pandas as pd
from flask import Flask, render_template, request

def get_similar_movies(movie_name, user_ratings):
    movie_name = movie_name.lower()
    if movie_name not in df['title'].unique():
        print("This movie is not in our dataset \nPlease try another movie")
    else:
        similar_score = item_similarity_df[movie_name]*(user_ratings-2.5)
        similar_score = similar_score.sort_values(ascending = False)
        return(similar_score.head(10))
        


get_similar_movies('star wars', 5)

