import spotipy
import credentials
import pandas as pd
from abc import ABC, abstractmethod

class SpotifyObj(ABC):

    def __init__(self, id:str):
        self.__id = id
        self.__spotify = spotipy.Spotify(
            auth_manager=spotipy.SpotifyOAuth(
            client_id=credentials.client_id(), 
            client_secret=credentials.client_secret(),
            redirect_uri="http://localhost"))

    @property
    def id(self):
        return self.__id

    @property
    def spotify(self):
        return self.__spotify 

    @abstractmethod
    def get_data(self):
        pass

