#Example Executed sucessfully
# define a list of songs and their genres
x = input("Enter the genre: ")
songs = [
    {"title": "Thriller", "artist": "Michael Jackson", "genre": "pop"},
    {"title": "Hotel California", "artist": "The Eagles", "genre": "rock"},
    {"title": "Bohemian Rhapsody", "artist": "Queen", "genre": "rock"},
    {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "genre": "rock"},
    {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "genre": "pop"},
    {"title": "All of Me", "artist": "John Legend", "genre": "pop"},
]

# define a function that takes in a genre and returns a list of songs in that genre
def get_recommendations(genre):
    recommendations = []
    for song in songs:
        if song["genre"] == genre:
            recommendations.append(song["title"])
    return recommendations

# test the recommendation function
#print(get_recommendations("pop"))
# Output: ["Thriller", "Uptown Funk", "All of Me"]
#print(get_recommendations("rock"))
# Output: ["Hotel California", "Bohemian Rhapsody", "Stairway to Heaven"]
print(get_recommendations(x))
