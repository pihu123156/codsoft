import pandas as pd

# Sample user-movie ratings
data = {
    'User': ['Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Charlie', 'Charlie', 'Charlie', 'Dave'],
    'Movie': ['Inception', 'Avatar', 'Titanic', 'Inception', 'Titanic', 'Avatar', 'Inception', 'Interstellar', 'Titanic'],
    'Rating': [5, 4, 3, 5, 2, 5, 3, 4, 5]
}

df = pd.DataFrame(data)
user_movie_matrix = df.pivot_table(index='User', columns='Movie', values='Rating')
from sklearn.metrics.pairwise import cosine_similarity

# Fill NaN with 0s for similarity calculation
filled_matrix = user_movie_matrix.fillna(0)

# Compute cosine similarity
user_similarity = cosine_similarity(filled_matrix)

# Put it back into a DataFrame
user_similarity_df = pd.DataFrame(user_similarity, index=filled_matrix.index, columns=filled_matrix.index)
def recommend_movies(user, num_recommendations=2):
    similar_users = user_similarity_df[user].sort_values(ascending=False)[1:]  # skip self

    weighted_ratings = pd.Series(dtype=float)
    
    for similar_user, similarity in similar_users.items():
        ratings = user_movie_matrix.loc[similar_user]
        weighted = ratings * similarity
        weighted_ratings = weighted_ratings.add(weighted, fill_value=0)

    # Remove movies already rated by the user
    rated_by_user = user_movie_matrix.loc[user].dropna().index
    recommendations = weighted_ratings.drop(labels=rated_by_user, errors='ignore')

    return recommendations.sort_values(ascending=False).head(num_recommendations)
print("Recommended for Alice:")
print(recommend_movies('Alice'))
