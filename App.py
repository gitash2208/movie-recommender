import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8'.format(movie_id))
    data=response.json()
    #print(data)
    return 'http://image.tmdb.org/t/p/w500/'+ data['poster_path']
movies_list=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_list)

def recommend(movie):
    movie_index =movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommendations_list = []
    recommended_movie_poster=[]
    for movie in movies_list:

       recommendations_list.append(movies.iloc[movie[0]].title)
       recommended_movie_poster.append(fetch_poster(movies.iloc[movie[0]].movie_id))
    return recommendations_list,recommended_movie_poster

similarity=pickle.load(open('similarity.pkl','rb'))
movies_title=movies['title'].values
st.title('Movies Recommender System')
selected_movie_name=st.selectbox(
    "Search Movie",
    movies_title
)
if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(names[0])
        st.image(posters[0])

    with col2:
        st.write(names[1])
        st.image(posters[1])
    with col3:
        st.write(names[2])
        st.image(posters[2])
    with col4:
        st.write(names[3])
        st.image(posters[3])
    with col5:
        st.write(names[4])
        st.image(posters[4])








