import unittest
from spotify_playlist import SpotifyPlaylist
from spotify_track import SpotifyTrack
from spotify_mock import SpotifyMock

class SpotifyPlaylistTest(unittest.TestCase):

    def setUp(self):
        self.mock = SpotifyMock()
        self.test_playlist = SpotifyPlaylist(self.mock.playlist_ID)
        self.test_playlist.get_data()

        self.test_track = SpotifyTrack(self.mock.track_ID)
        self.test_track.get_data()

    def test_playlist_name(self):
        self.assertEqual(self.test_playlist.name, self.mock.playlist_name)

    def test_playlist_owner(self):
        self.assertEqual(self.test_playlist.owner, self.mock.playlist_owner)

    def test_playlist_track(self):
        tester = False
        for track in self.test_playlist.tracks:
            if track.id == self.test_track.id and track.title == self.test_track.title:
                tester = True
        self.assertTrue(tester)

