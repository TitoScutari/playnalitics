import unittest
from spotify_playlist import SpotifyPlaylist
from spotify_track import SpotifyTrack
from spotify_mock import SpotifyMock

class SpotifyPlaylistTest(unittest.TestCase):

    def setUp(self):
        self.mock = SpotifyMock()
        self.test_playlist = SpotifyPlaylist(self.mock.playlist_ID).get_data()
        self.test_track = SpotifyTrack(self.mock.track_ID).get_data()

    def test_playlist_name(self):
        self.assertEqual(self.test_playlist.name, "test")

    def test_playlist_owner(self):
        self.assertEqual(self.test_playlist.owner, self.mock.playlist_owner)

    def test_playlist_track(self):
        self.assertIn(self.test_track, self.test_playlist.tracks)

