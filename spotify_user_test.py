import unittest
from spotify_playlist import SpotifyPlaylist
from spotify_user import SpotifyUser
from spotify_mock import SpotifyMock

class SpotifyUserTest(unittest.TestCase):

    def setUp(self):
        self.mock = SpotifyMock()
        self.test_user = SpotifyUser(current=True)
        self.test_user.get_data()

    def test_user_name(self):
        self.assertEqual(self.test_user.name, self.mock.user_name)

    def test_user_playlist(self):
        tester = False
        for playlist in self.test_user.playlists:
            if self.mock.playlist_name == playlist.name and self.mock.playlist_ID == playlist.id:
                tester = True
        self.assertTrue(tester)
