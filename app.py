
# import streamlit as st

# import pickle
# import requests

# movies = pickle.load(open("movies_list.pk1", 'rb'))
# similarity = pickle.load(open("similarity.pk1", 'rb'))

# movies_list = movies['title'].values



# st.header("Movie Recommender System")
# selectvalue=st.selectbox("Select movie from dropdown", movies_list)

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/discover/movie?api_key=195313f4563ea9952e895a0423f91a2e"
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_paht']
#     full_path = "https://image.tmdb.org/t/p/w500/1E5baAaEse26fej7uHcjOgEE2t2.jpg" +poster_path
#     return full_path
    


# # movies_list = movies['title'].values
# def recommand(movie):
#     index = movies[movies['title']==movie].index[0]
#     distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
#     recommand_movie = []
#     recommand_poster= []
#     for i in distance[1:6]:
#         movies_id = movies.iloc[i[0]].id
#         recommand_movie.append(movies.iloc[i[0]].title)
#         recommand_poster.append(fetch_poster(movies_id))
        
#     return recommand_movie, recommand_poster
#         # print(movies.iloc[i[0]].title)










# if st.button("Show Recommend"):
#     movie_name , movie_poster= recommand(selectvalue)
#     col1, col2, col3, col4, col5= st.columns(5)
#     with col1:
#         st.text(movie_name[0])
#         st.image(movie_poster[0])
#     with col2:
#         st.text(movie_name[1])
#         st.image(movie_poster[1])
#     with col3:
#         st.text(movie_name[2])
#         st.image(movie_poster[2])
#     with col4:
#         st.text(movie_name[3])
#         st.image(movie_poster[3])
#     with col5:
#         st.text(movie_name[4])
#         st.image(movie_poster[4])
#     # with col6:
#     #     st.text(movie_name[5])
    
#     # pass















import streamlit as st
import pickle
import requests


movies = pickle.load(open("movies_list.pk1", 'rb'))
similarity = pickle.load(open("similarity.pk1", 'rb'))


movies_list = movies['title'].values


st.header("Movie Recommender System")
selectvalue = st.selectbox("Select movie from dropdown", movies_list)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=195313f4563ea9952e895a0423f91a2e"
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path', '')
    full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
    return full_path

def recommand(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommand_movie = []
    recommand_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommand_movie.append(movies.iloc[i[0]].title)
        recommand_poster.append(fetch_poster(movie_id))
    return recommand_movie, recommand_poster

if st.button("Show Recommend"):
    movie_name, movie_poster = recommand(selectvalue)
    cols = st.columns(5)
    for col, name, poster in zip(cols, movie_name, movie_poster):
        with col:
            st.text(name)
            st.image(poster)


