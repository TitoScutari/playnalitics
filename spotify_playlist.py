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
        playlist_data = self.__spotify.playlist_tracks(self.id)
        self.__name = playlist_data["name"]
        self.__owner = playlist_data["owner"]
        self.__tracks = [SpotifyTrack(track_id).get_data() for track_id in playlist_data["track_ids"]]
