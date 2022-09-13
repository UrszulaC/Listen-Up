import streamlit as st
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import visualizer
import trackrecommendations

# integrating spotify library and creating, sp object using login client credentials
cid = 'cc93ac994d624b09a151d5beac39b528'
secret = 'f41147cfcc1f48ccabf93263c305eac1'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
spotipy_Spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

st.header('Listen Up!')

# main search options with keyword search
search_options = ['Song/Track', 'Artist', 'Album']
search_selected = st.sidebar.selectbox("Your search choice please: ", search_options)

# input with keyword search
search_word = st.text_input(search_selected + " (Keyword Search)")
button_search = st.button("Search")

search_results = []
tracks = []
artists = []
albums = []


# song/track search with keyword displaying the track and 20 additional suggestions
if search_word is not None and len(str(search_word)) > 0:
    if search_selected == 'Song/Track':
        # st.write("Start song/track search")
        tracks = spotipy_Spotify.search(q='track:' + search_word, type='track', limit=20)
        tracks_list = tracks['tracks']['items']
        if len(tracks_list) > 0:
            for track in tracks_list:
                # st.write(track['name'] + " - By - " + track['artists'][0]['name'])
                search_results.append(track['name'] + " - By - " + track['artists'][0]['name'])

    # artist object created displaying 20 suggested artist based on typed keyword
    elif search_selected == 'Artist':
        artists = spotipy_Spotify.search(q='artist:' + search_word, type='artist', limit=20)
        artists_list = artists['artists']['items']
        if len(artists_list) > 0:
            for artist in artists_list:
                # st.write(artist['name'])
                search_results.append(artist['name'])

    # album object created displaying 20 suggested albums based on typed keyword
    if search_selected == 'Album':
        albums = spotipy_Spotify.search(q='album:' + search_word, type='album', limit=20)
        albums_list = albums['albums']['items']
        if len(albums_list) > 0:
            for album in albums_list:
                # st.write(album['name'] + " - By - " + album['artists'][0]['name'])
                # print("Album ID: " + album['id'] + " / Artist ID - " + album['artists'][0]['id'])
                search_results.append(album['name'] + " - By - " + album['artists'][0]['name'])

# search options to select: tracks, artist, album
chosen_album = None
chosen_artist = None
chosen_track = None

if search_selected == 'Song/Track':
    chosen_track = st.selectbox("Select the song/track: ", search_results)
elif search_selected == 'Artist':
    chosen_artist = st.selectbox("Select the artist: ", search_results)
elif search_selected == 'Album':
    chosen_album = st.selectbox("Select the album: ", search_results)

if chosen_track is not None and len(tracks) > 0:
    tracks_list = tracks['tracks']['items']
    track_id = None
    if len(tracks_list) > 0:
        for track in tracks_list:
            str_temp = track['name'] + " - By - " + track['artists'][0]['name']
            if str_temp == chosen_track:
                track_id = track['id']
                track_album = track['album']['name']
                img_album = track['album']['images'][1]['url']
                trackrecommendations.save_album_image(img_album, track_id)

    # if track is selected returning image of the album by track id
    if track_id is not None:
        image = trackrecommendations.get_album_image(track_id)
        st.image(image)
        track_choices = ['Song Features', 'Songs Recommendation']
        selected_track_choice = st.sidebar.selectbox('Please select the track: ', track_choices)
        # adding selected features to display with features visualizer
        if selected_track_choice == 'Song Features':
            track_features = spotipy_Spotify.audio_features(track_id)
            df = pd.DataFrame(track_features, index=[0])
            df_features = df.loc[:, ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence']]
            st.dataframe(df_features)
            visualizer.feature_plot(df_features)

        # song recommendation listed based on matching features
        elif selected_track_choice == 'Similar Songs Recommendation':
            token = trackrecommendations.show_token(cid, secret)
            similar_songs_json = trackrecommendations.show_track_recommendations(track_id, token)
            recommendation_list = similar_songs_json['tracks']
            recommendation_list_df = pd.DataFrame(recommendation_list)
            # st.dataframe(recommendation_list_df)
            recommendation_df = recommendation_list_df[['name', 'explicit', 'duration_ms', 'popularity']]
            st.dataframe(recommendation_df)
            # st.write("Recommendations....")
            trackrecommendations.song_recommendation_visualiser(recommendation_df)

    else:
        st.write("Please select a track from the list")

# album integration, when album is selected (id and uri shown) and tracks
elif chosen_album is not None and len(albums) > 0:
    albums_list = albums['albums']['items']
    album_id = None
    album_uri = None
    album_name = None
    if len(albums_list) > 0:
        for album in albums_list:
            str_temp = album['name'] + " - By - " + album['artists'][0]['name']
            if chosen_album == str_temp:
                album_id = album['id']
                album_uri = album['uri']
                album_name = album['name']

    # collecting tracks from the album and displaying with selected features
    if album_id is not None and album_uri is not None:
        st.write("Collecting all the tracks for the album: " + album_name)
        album_tracks = spotipy_Spotify.album_tracks(album_id)
        df_album_tracks = pd.DataFrame(album_tracks['items'])
        # st.dataframe(df_album_tracks)
        df_tracks_min = df_album_tracks.loc[:, ['id', 'name', 'duration_ms', 'explicit', 'preview_url']]

        # streamlit container displaying id, name, time, if explicit and audio track preview
        for idx in df_tracks_min.index:
            with st.container():
                col1, col2, col3, col4 = st.columns((4, 4, 1, 1))
                col11, col12 = st.columns((8, 2))
                col1.write(df_tracks_min['id'][idx])
                col2.write(df_tracks_min['name'][idx])
                col3.write(df_tracks_min['duration_ms'][idx])
                col4.write(df_tracks_min['explicit'][idx])
                if df_tracks_min['preview_url'][idx] is not None:
                    col11.write(df_tracks_min['preview_url'][idx])
                    with col12:
                        st.audio(df_tracks_min['preview_url'][idx], format="audio/mp3")

# artist integration
if chosen_artist is not None and len(artists) > 0:
    artists_list = artists['artists']['items']
    artist_id = None
    artist_uri = None
    selected_artist_choice = None
    if len(artists_list) > 0:
        for artist in artists_list:
            if chosen_artist == artist['name']:
                artist_id = artist['id']
                artist_uri = artist['uri']

    # sidebar options when artist selected in main search
    if artist_id is not None:
        artist_choice = ['Albums', 'Top Songs']
        selected_artist_choice = st.sidebar.selectbox('Select artist choice', artist_choice)

    # displaying Album options for the selected artist (showing album name, release day and number of tracks)
    if selected_artist_choice is not None:
        if selected_artist_choice == 'Albums':
            artist_uri = 'spotify:artist:' + artist_id
            album_result = spotipy_Spotify.artist_albums(artist_uri, album_type='album')
            all_albums = album_result['items']
            col1, col2, col3 = st.columns((6, 4, 2))
            for album in all_albums:
                col1.write(album['name'])
                col2.write(album['release_date'])
                col3.write(album['total_tracks'])

        # displaying 'Top Songs' options for selected Artist
        elif selected_artist_choice == 'Top Songs':
            artist_uri = 'spotify:artist:' + artist_id
            top_songs_result = spotipy_Spotify.artist_top_tracks(artist_uri)
            for track in top_songs_result['tracks']:
                with st.container():
                    col1, col2, col3, col4 = st.columns((4, 4, 2, 2))
                    col11, col12 = st.columns((10, 2))
                    col21, col22 = st.columns((11, 1))
                    col31, col32 = st.columns((11, 1))
                    col1.write(track['id'])
                    col2.write(track['name'])
                    # link with audio preview
                    if track['preview_url'] is not None:
                        col11.write(track['preview_url'])
                        with col12:
                            st.audio(track['preview_url'], format="audio/mp3")

                    # displaying selected features for the track
                    with col3:
                        def feature_requested():
                            track_features = spotipy_Spotify.audio_features(track['id'])
                            df = pd.DataFrame(track_features, index=[0])
                            df_features = df.loc[:,
                                          ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness',
                                           'speechiness', 'valence']]
                            with col21:
                                st.dataframe(df_features)
                            with col31:
                                visualizer.feature_plot(df_features)


                        feature_button_state = st.button('Track Audio Features', key=track['id'],
                                                         on_click=feature_requested)
                    with col4:
                        # recommending similar songs based on features selected (displaying name, explicit, duration,
                        # popularity of recommended songs

                        def similar_songs_requested():
                            token = trackrecommendations.show_token(cid, secret)
                            similar_songs_json = trackrecommendations.show_track_recommendations(track['id'], token)
                            recommendation_list = similar_songs_json['tracks']
                            recommendation_list_df = pd.DataFrame(recommendation_list)
                            recommendation_df = recommendation_list_df[
                                ['name', 'explicit', 'duration_ms', 'popularity']]
                            with col21:
                                st.dataframe(recommendation_df)
                            with col31:
                                trackrecommendations.song_recommendation_visualiser(recommendation_df)


                        similar_songs_state = st.button('Similar Songs', key=track['id'],
                                                        on_click=similar_songs_requested)
                    st.write('----')
