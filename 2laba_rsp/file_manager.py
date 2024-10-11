import json
from musical_composition import Track
from album import Album

def load_album_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            album = Album(data['title'])
            for track_data in data['tracks']:
                track = Track(track_data['title'], track_data['duration'], track_data['style'], track_data['artist'])
                album.add_track(track)
            return album
    except FileNotFoundError:
        return Album("New Album")

def save_album_data(album, filename):
    with open(filename, 'w') as file:
        data = {
            'title': album.title,
            'tracks': [{'title': track.title, 'duration': track.duration, 'style': track.style, 'artist': track.artist} for track in album.tracks]
        }
        json.dump(data, file)
