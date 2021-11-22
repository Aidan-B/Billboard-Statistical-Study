import spotify_api as s
import json

albums = s.get_albums(
    s.get_artist_albums(
        s.get_artist_id("pitbull")
    )
)

# for album in albums:
#     print album

for name in [ album['name'] for album in albums ]:    
    print(name)

# print(spotify_api.get_tracks("3rfhI32Il2hVRKDkuGeeen,13plQdOoWSSXPRUSZc5FuM"))