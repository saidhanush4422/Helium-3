import pandas as pd
import numpy as np

a= int(input("Please rate your current mood so that we can send you a recommendation : "))
b= int(input("Please rate your current mood so that we can send you a recommendation : "))
c= (a+b)/2
d= int(input("Enter what you want to do from the options: "))

data = pd.read_csv("data.csv")
def recommend_songs(value):
  # Get all the songs by the val.
  songs_by_artist = data[data["c"] == value]["songs"]

  # Get all the songs by similar artists
  similar_artists = data[data["c"] != value]["c"].unique()
  songs_by_similar_artists = data[data["c"].isin(similar_artists)]["songs"]

  # Recommend the top 10 most popular songs by similar artists
  recommendations = songs_by_similar_artists.value_counts().head(10)

  # Remove any songs by the original artist from the recommendations
  recommendations = recommendations[~recommendations.isin(songs_by_artist)]

  return recommendations

def recommend_movies(value):
movie_by_genre = data[data["c"] == value]["movies"]

similar_genre = data[data["c"] != value]["c"].unique()
  movies_by_similar_genres = data[data["c"].isin(similar_genre)]["movies"]

recommendations = movies_by_similar_genres.value_counts().head(10)

recommendations = recommendations[~recommendations.isin(movie_by_genre)]

  return recommendations

def recommend_books(value):
 books_by_author = data[data["c"] == value]["books"]

 similar_author = data[data["c"] != value]["c"].unique()
  books_by_similar_authors = data[data["c"].isin(similar_author)]["books"]

 recommendations = books_by_similar_authors.value_counts().head(10)

 recommendations = recommendations[~recommendations.isin(songs_by_artist)]

  return recommendations

#option for user
actions = {
    1: lambda: print("You entered songs"),
    2: lambda: print("You entered movies"),
    3: lambda: print("You entered books"),
}

actions.get(d, lambda: print("Invalid input"))()


if d == 1:
    print(recommend_songs(c))
elif d == 2:
    print(recommend_movies(c))
elif d == 3:
    print(recommend_books(c))
else:
    print("Invalid input")
