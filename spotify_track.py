from spotify_obj import SpotifyObj

class SpotifyTrack(SpotifyObj):

    def __init__(self, id: str):
        super().__init__(id)

    
    @property
    def title(self):
        return self.__title
    
    @property
    def artist(self):
        return self.__artist
    
    @property
    def key(self):
        return self.__key
    
    @property
    def bpm(self):
        return self.__bpm
    
    @property
    def valence(self):
        return self.__valence
    
    @property
    def loudness(self):
        return self.__loudness
    
    @property
    def acousticness(self):
        return self.__acousticness
    
    @property
    def danceability(self):
        return self.__danceability
    
    @property
    def energy(self):
        return self.__energy

    def get_data(self):
        track_data = self.__spotify.audio_features()
        self.__title = track_data["title"]
        self.__artist = track_data["artist"]
        self.__key = track_data["key"]
        self.__bpm = track_data["bpm"]
        self.__valence = track_data["valence"]
        self.__loudness = track_data["loudness"]
        self.__acousticness = track_data["acousticness"]
        self.__danceability = track_data["danceability"]
        self.__energy = track_data["energy"]
