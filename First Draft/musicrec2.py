#Executed sucessfully
# Import the necessary libraries
import pandas as pd
import numpy as np

a=input("Enter the artist_name: ")
# Load the data
data = pd.read_csv("music_data.csv")

# Define a function to recommend songs based on similar artists
def recommend_songs(artist):
  # Get all the songs by the artist
  songs_by_artist = data[data["artist_name"] == artist]["tempo"]

  # Get all the songs by similar artists
  similar_artists = data[data["artist_name"] != artist]["artist_name"].unique()
  songs_by_similar_artists = data[data["artist_name"].isin(similar_artists)]["tempo"]

  # Recommend the top 10 most popular songs by similar artists
  recommendations = songs_by_similar_artists.value_counts().head(10)

  # Remove any songs by the original artist from the recommendations
  recommendations = recommendations[~recommendations.isin(songs_by_artist)]

  return recommendations

# Test the recommendation function
print(recommend_songs(a))
