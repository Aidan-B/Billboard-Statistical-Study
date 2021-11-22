import spotify_api as s

import json



albums = s.get_albums(
    s.get_artist_albums(
        s.get_artist_id("pitbull")
    )
)

print(s.get_track_id("Runaway Baby"))

# for album in albums:
#     print album
for name in [ album['name'] for album in albums ]:    
    print(name)