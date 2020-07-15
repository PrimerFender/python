tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
                      "On the Other Side": "Samara"},
          "Cure": {"Disintegration": "Lovesong",
                   "Wish": "Friday I'm in love",
                   "Seventeen Seconds": "A Forest"}}

def tracklist(**kwargs):
    for artist, songs in kwargs.items():
        print(artist)
        for album, track in songs.items():
            print("ALBUM:", album, "TRACK:", track)

tracklist(Woodkid={"The Golden Age": "Run Boy Run",
                   "On the Other Side": "Samara"},
          Cure={"Disintegration": "Lovesong",
                "Wish": "Friday I'm in love",
                "Seventeen Seconds": "A Forest"})