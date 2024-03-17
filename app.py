import pickle
import streamlit as st

def recommend(game):
    index = games[games['Name'] == game].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_games = []
    seen_games = set()
    for i in distances[1:]:
        game_name = games.iloc[i[0]].Name
        if game_name not in seen_games:
            recommended_games.append(game_name)
            seen_games.add(game_name)
        if len(recommended_games) >= 5:
            break
    if game in recommended_games:
        recommended_games.remove(game)
        recommended_games.append(games.iloc[distances[6][0]].Name)
    return recommended_games




st.header('Game Recommender System')
games = pickle.load(open('game_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

game_list = games['Name'].values
selected_game = st.selectbox(
    "Type or select a game from the dropdown",
    game_list
)

if st.button('Show Recommendation'):
    recommended_games = recommend(selected_game)
    for game in recommended_games:
        st.write(game)
