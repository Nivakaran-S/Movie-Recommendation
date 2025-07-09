import pickle
import streamlit as st 
import requests 

st.header("Movie recommendation system")

movies = pickle.load(open('./artifacts/movie_list.pkl', 'rb'))
similarity_score = pickle.load(open('./artifacts/similarity.pkl', 'rb'))

movie_list = movies['title'].values

selected_movie = st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity_score[index])), reverse=True, key=lambda x: x[1])
    for i in distances[1:6]:
        print(movies.iloc[i[0]].title)

if st.button('Show recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)