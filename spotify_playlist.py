from spotify_obj import SpotifyObj
from spotify_track import SpotifyTrack

class SpotifyPlaylist(SpotifyObj):
    
    def __init__(self, id: str):
        super().__init__(id)

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def owner(self) -> str:
        return self.__owner
    
    @property
    def tracks(self) -> list :
        return self.__tracks
    
    #TODO indexing need fix
    def get_data(self):
        playlist_data = self.spotify.playlist(self.id)
        self.__name = playlist_data["name"]
        self.__owner = playlist_data["owner"]["id"]
        self.__tracks = [SpotifyTrack(track["track"]["id"]) for track in playlist_data["tracks"]["items"]]
        for track in self.__tracks:
            track.get_data()
