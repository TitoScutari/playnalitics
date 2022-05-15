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
        track_features = self.spotify.audio_features(self.id)
        track_data = self.spotify.track(self.id)
        self.__title = track_data["name"]
        self.__artist = track_data["artists"][0]["name"]
        self.__key = track_features[0]["key"]
        self.__bpm = track_features[0]["tempo"]
        self.__valence = track_features[0]["valence"]
        self.__loudness = track_features[0]["loudness"]
        self.__acousticness = track_features[0]["acousticness"]
        self.__danceability = track_features[0]["danceability"]
        self.__energy = track_features[0]["energy"]
