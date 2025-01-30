import streamlit as st
from core import recommend, new_df

movies_list = new_df['title'].values

# Title of webpage
st.title("Movie Recommendation System")

# About movie recommendation system
st.text("A Movie Recommendation System designed to suggest similar movies based on user-selected preferences.")

# Dropbox selection
selected_movies = st.selectbox(
    "Select Movie",
    movies_list,
)

if st.button("Recommend", type="primary"):
    names, poster = recommend(selected_movies)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(poster[0])
        st.text(names[0])

    with col2:
        st.image(poster[1])
        st.text(names[1])

    with col3:
        st.image(poster[2])
        st.text(names[2])
    
    with col4:
        st.image(poster[3])
        st.text(names[3])

    with col5:
        st.image(poster[4])
        st.text(names[4])