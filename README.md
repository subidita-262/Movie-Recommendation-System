# Movie-Recommendation-System
It’s a website that recommends movies based on user’s choice and ratings on other movies, using collaborative filtering algorithm, classifies based on the sentiment of reviews, using sentiment analysis. 
also, shows the movie review statistics.
## Project Description
  Recommends Movies based on the user ratings.
  Classifies the sentiment of reviews into negative or positive.
  Uses this model to show the movie statistics.
## Personal contribution
  Creating the Recommendation engine.
  Designing the website using html, css, flask.
## Functionality And Modules
### Data Pre-processing
Dataset – Movie lens dataset (Kaggle)
Columns – user_id, item_id, ratings, timestamp
Merge Movie_id_titles dataset on unique item_id
### Data analysis
Make a pivot table with user_id, Movies, average ratings.
### Recommend Movies
Only consider movies with more than 100 user ratings (Setting threshold).
Find correlation based on the movies with the pivot table using Pearson Method which standardize all the ratings.
Higher the correlation that  movie will be mostly recommended.
## Applications
Recommend movies based on user ratings on unique items that is static.
Analyse the sentiment of user input which decreases the chance of fake reviews.
Store the data in table using SQL.
Show movie statistics to a user.
Profile points of users for reliability.
## Challenges & future Improvements
Handling unknown users and items (Cold Start Problem)
Combine Content based recommender system with collaborative system to create a Hybrid system.
  Data Sparsity
  Scalability
  Dynamic updates
Rebuilding the model is a challenge for new items.


