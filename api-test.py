import requests
import pytest
import os
import dotenv
import json

apiurl = "https://api.musixmatch.com/ws/1.1/"
apikey = os.environ['APIKEY']



def test_top10_artists():
    path = "page=1&page_size=10&country=mx"
    req = requests.get(f'{apiurl}chart.artists.get?{path}&apikey={apikey}')
    a_list = req.json()['message']['body']['artist_list']
    for artist in a_list:
        print (artist["artist"]["artist_name"])
    assert req.status_code == 200

def test_top3_info():
    path = "page=1&page_size=3&country=mx"
    req = requests.get(f'{apiurl}chart.artists.get?{path}&apikey={apikey}')
    a_list = req.json()['message']['body']['artist_list']
    for artist in a_list:
        print(artist["artist"]["artist_name"], json.dumps(artist["artist"], indent=4))

    assert req.status_code == 200

def test_top_5_albums():
    path = "artist_id=5"
    req = requests.get(f'{apiurl}artist.albums.get?{path}&apikey={apikey}')
    al_list = req.json()['message']['body']['album_list']
    for album in al_list:
        print(album['album']['album_name'])

    assert req.status_code == 200


















