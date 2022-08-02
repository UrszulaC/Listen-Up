import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'cc93ac994d624b09a151d5beac39b528'
secret = 'f41147cfcc1f48ccabf93263c305eac1'

client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret = secret)

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

sp.me

albums = sp.search(q='album:'+'love', type='album', limit=20)

albums_list = albums['albums']['items']
if len(albums_list) > 0:
    for album in albums_list:
        print(album['name'] + " - By - " + album["artists"][0]["name"])
        print("Album ID: " + album["id"] + " /Artist ID - " + album["artists"][0]["id"])
        print("------")

artist_id = "3TVXtAsR1Inumwj472S9r4"

artist_uri = "spotify:artist:" + artist_id
results = sp.artist_albums(artist_uri, album_type="album", limit=5)
albums = results["items"]
while results["next"]:
    results = sp.next(results)
    albums.extend(results["items"])

albums[0]["artists"][0]["name"]
for album in albums:
    print(album["name"] + " (Artist: " + album["artists"][0]["name"] + " ).")



