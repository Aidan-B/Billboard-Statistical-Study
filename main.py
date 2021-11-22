import spotify_api as s
import json

albums = json.load(
    s.get_albums(
        s.get_artist_albums(
            s.get_artist_id("pitbull")
        )
    )
)

print(s.get_track_id("Runaway Baby"))

print(albums[0]['name'])
# print(spotify_api.get_tracks("3rfhI32Il2hVRKDkuGeeen,13plQdOoWSSXPRUSZc5FuM"))