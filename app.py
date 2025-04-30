import pickle
import streamlit as st
import requests
import json

def fetch_poster(movie_title):
    url = "https://movie-database-alternative.p.rapidapi.com/"
    
    headers = {
        "x-rapidapi-host": "movie-database-alternative.p.rapidapi.com",
        "x-rapidapi-key": "58a58f5ec8msh7a5fd68774cbb01p1928d1jsn4a29a93d1284" 
    }
    
    params = {
        "s": movie_title,
        "r": "json",
        "page": "1"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.ok:
            data = json.loads(response.text)
            if data.get("Response") == "True" and data.get("Search"):

                poster_url = data["Search"][0].get("Poster")
                if poster_url != "N/A":
                    return poster_url
        return None
    except (requests.RequestException, json.JSONDecodeError):
        return None

def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movies = []
        
        for i in distances[1:6]:
            title = movies.iloc[i[0]].title
            poster = fetch_poster(title)
            recommended_movies.append({
                'title': title,
                'poster': poster if poster else "https://via.placeholder.com/300x450?text=No+Poster"
            })
        
        return recommended_movies
    except (IndexError, AttributeError):
        return []

# Page config
st.set_page_config(page_title="Movie Recommender System", layout="wide")
st.header('Movie Recommender System')

# Load data
try:
    movies = pickle.load(open('model/movie_list.pkl', 'rb'))
    similarity = pickle.load(open('model/similarity.pkl', 'rb'))
    movie_list = movies['title'].values
except (FileNotFoundError, pickle.PickleError):
    st.error("Error: Could not load movie data. Please check if the model files exist.")
    st.stop()

# Movie selection
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    with st.spinner('Fetching recommendations...'):
        recommended_movies = recommend(selected_movie)
        
        if recommended_movies:
            cols = st.columns(5)
            for col, movie in zip(cols, recommended_movies):
                with col:
                    st.text(movie['title'])
                    st.image(movie['poster'])
        else:
            st.error("Could not generate recommendations. Please try another movie.")
