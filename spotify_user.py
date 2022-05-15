from spotify_obj import SpotifyObj
from spotify_playlist import SpotifyPlaylist

class SpotifyUser(SpotifyObj):
    
    def __init__(self, id: str):
        super().__init__(id)

    @property
    def name(self):
        return self.__name
    
    @property
    def playlists(self):
        return self.__playlists
    
    def get_data(self):
        user_data = self.__spotify.user(self.id)

        # this one needs work, we want user_playlist to be a list of playlist_IDs
        user_playlists = self.__spotify.user_playlists(self.id)
        
        #TODO undestand and make dictionary indexing right
        self.__name = user_data["name"]
        self.__playlists = [SpotifyPlaylist(playlist_id).get_data() for playlist_id in user_playlists]
        
