import pymysql
from spotify_track import SpotifyTrack
from spotify_playlist import SpotifyPlaylist
from spotify_user import SpotifyUser

class playnaliticsDB:

    def __init__(self) -> None:
        self.__hostname = 'localhost'
        self.__username = 'root'
        self.__password = ''
        self.__database = 'playnaliticsDB'

    def connect(self):
        self.__connection = pymysql.connect(
            host=self.__hostname, 
            user=self.__username, 
            passwd=self.__password, 
            db=self.__database
            )
        self.__cursor = self.__connection.cursor()

    def close(self, commit:bool = False):
        if commit:
            self.__connection.commit()
            self.__connection.close()

    def clean(self):
        self.__cursor.execute(
            """
            TRUNCATE playlist
            TRUNCATE tracks
            TRUNCATE playlisttracks
            """
        )

    def insert_track(self, track:SpotifyTrack):
        sql = """INSERT INTO tracks VALUES(%s, %s, %s, %f, %f, %f, %f, %f, %d, %f)"""
        self.__cursor.execute(
            sql, 
            track.id, 
            track.title, 
            track.artist, 
            track.acousticness, 
            track.danceability, 
            track.energy,
            track.valence,
            track.loudness,
            track.key,
            track.bpm
            )
        
    def insert_playlist(self, playlist:SpotifyPlaylist):
        sql_playlists = """INSERT INTO playlists VALUES(%s, %s, %s)"""
        sql_playlist_tracks = """"INSERT INTO playlisttracks VALUES(%s, %s)"""
        self.__cursor.execute(sql_playlists, playlist.id, playlist.owner, playlist.name)
        for track in playlist.tracks:
            self.insert_track(track)
            self.__cursor.execute(sql_playlist_tracks, playlist.id, track.id)

    def insert_user(self, user:SpotifyUser):
        for playlist in user.playlists:
            self.insert_playlist(playlist)

    def select_playlists(self, user_id):
        sql = """
        SELECT playlists.id playlists.name
        FROM playlists
        WHERE playlists.owner = %s
        """
        self.__cursor.execute(sql, user_id)
        return self.__cursor.fetchall()

    def select_playlist_tracks(self, playlist_id):
        sql = """
        SELECT *
        FROM tracks
        INNER JOIN playlisttracks
        ON tracks.Id = playlisttracks.IdTrack
        WHERE IdPlaylist = %s
        """
        self.__cursor.execute(playlist_id)
        return self.__cursor.fetchall()