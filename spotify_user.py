from spotify_obj import SpotifyObj
from spotify_playlist import SpotifyPlaylist

class SpotifyUser(SpotifyObj):
    
    def __init__(self, id: str = '', current:bool = False):
        super().__init__(id)
        if current:
            id = self.spotify.current_user()["id"]
        super().__init__(id)

    @property
    def name(self):
        return self.__name
    
    @property
    def playlists(self):
        return self.__playlists
    
    def get_data(self):

        user_data = self.spotify.user(self.id)
        self.__name = user_data["display_name"]

        user_playlists = self.spotify.user_playlists(self.id)
        
        #TODO undestand and make dictionary indexing right
        self.__playlists = [SpotifyPlaylist(playlist["id"]) for playlist in user_playlists["items"]]
        for playlist in self.__playlists:
            playlist.get_data()
        
