from src.helper import basic_preprocess, clean, extract_crew_director, extract_top3_cast, stem, fetch_poster
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies_data = pd.read_csv(r"data\tmdb_5000_movies.csv")
credits_data = pd.read_csv(r"data\tmdb_5000_credits.csv")

# Merge
data = movies_data.merge(credits_data, on='title')

# Content Based Recommendation System
""" 
### Creating tags for similarity 
1. Genre
2. id
3. keywords
4. title
5. overview
6. cast 
7. crew
"""
movies = data[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

# Basic Preprocessing
movies = basic_preprocess(movies)

# Advance Cleaning
movies['genres'] = movies['genres'].apply(clean)
movies['keywords'] = movies['keywords'].apply(clean)
movies['cast'] = movies['cast'].apply(extract_top3_cast)
movies['crew'] = movies['crew'].apply(extract_crew_director)
movies['overview'] = movies['overview'].apply(lambda x: [x])

# Removing spaces to avoid misconception between names
movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

# Creating tags column
movies['tags'] = movies['overview'] + movies['cast'] + movies['crew'] + movies['genres'] + movies['keywords']
new_df = movies[['movie_id', 'title', 'tags']]
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

# Stemming operation
new_df['tags'] = new_df['tags'].apply(stem)

# Vectorization of words (BOWs)
cv = CountVectorizer(max_features=10000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

# Similarity between vectors
similarity = cosine_similarity(vectors) # (4806, 4806) size similarity vector

###################################################### MAIN LOGIC OF RECOMMENDATION ##############################################################

# Recommendation of 5 movies
def recommend(movie):
    idx = new_df[new_df['title'] == movie].index[0]
    distances = similarity[idx]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = new_df.iloc[i[0]].movie_id

        # fetching poster of movie
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies.append(new_df.iloc[i[0]].title)
    return recommended_movies, recommended_movies_poster