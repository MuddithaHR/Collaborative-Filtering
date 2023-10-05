import pickle
import streamlit as st
import pandas as pd

st.markdown("<h1 style='text-align: center; color: rgb(204, 238, 255);'>Movie Recommender System</h1>", unsafe_allow_html=True)
movies = pickle.load(open('movieRatings.pkl','rb'))
similarity = pickle.load(open('similarityMatrix.pkl','rb'))

movie_list = movies.columns
rate_list = [1,2,3,4,5]

col1, col2 = st.columns(2,gap='large')
with col1:
    selected_movie1 = st.selectbox("Type or select a movie from the dropdown", movie_list)
    selected_movie2 = st.selectbox("", movie_list)
    selected_movie3 = st.selectbox(" ", movie_list)

with col2:
    movie1 = st.selectbox("Rate the movie", rate_list)
    movie2 = st.selectbox("", rate_list)
    movie3 = st.selectbox(" ", rate_list)

# print(movie_list)
def get_similar(movie_name, rating):
    similar_ratings = similarity[movie_name]*(rating - 2.5)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    #print(type(similar_ratings))
    return similar_ratings


rating_list = [(selected_movie1,movie1),(selected_movie2,movie2),(selected_movie3,movie3)]

def get_movies(list):
    similar_movies = pd.DataFrame(columns = movie_list)
    for movie,rating in list:
        similar_movies.loc[len(similar_movies)] = get_similar(movie,rating)
    return similar_movies.sum().sort_values(ascending=False).head(8)

if st.button('Show Similar Movies'):
    rating_list = [(selected_movie1,movie1),(selected_movie2,movie2),(selected_movie3,movie3)]
    recommended = get_movies(rating_list).index.tolist()
    n = 0
    for film in recommended:
        if n < 5:
            if film not in [selected_movie1, selected_movie2, selected_movie3] :  
                st.markdown(film)
                n += 1

hide_st_style=""" 

<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""


