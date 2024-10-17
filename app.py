import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]


#is function ka kaam yeh ki agar apne isko movie di to vo apko palat k 5 movie l naam degi
    recommended_movies=[]
    for i in movies_list:
        movie_id= i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommander Systumm')

import streamlit as st

selected_movie_name = st.selectbox(
"How would you like to be contacted?",
movies['title'].values)

if st.button('Recommend'):
    recommendations= recommend(selected_movie_name)
    for i in recommendations:
      st.write(i)