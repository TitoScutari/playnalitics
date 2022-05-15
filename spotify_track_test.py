import unittest
from spotify_track import SpotifyTrack
from spotify_mock import SpotifyMock

class SpotifyTrackTest(unittest.TestCase):

    def setUp(self) -> None:
        self.mock = SpotifyMock()
        self.test_track = SpotifyTrack(self.mock.track_ID).get_data()
    
    def test_track_title(self):
        self.assertEqual(self.test_track.title, self.mock.title)

    def test_track_artist(self):
        self.assertEqual(self.test_track.artist, self.mock.artist)

    def test_track_key(self):
        self.assertEqual(self.test_track.key, self.mock.key)

    def test_track_bpm(self):
        self.assertEqual(self.test_track.bpm, self.mock.bpm)

    def test_track_valence(self):
        self.assertEqual(self.test_track.valence , self.mock.valence)

    def test_track_loudness(self):
        self.assertEqual(self.test_track.loudness , self.mock.loudness)

    def test_track_acousticness(self):
        self.assertEqual(self.test_track.acousticness , self.mock.acousticness)

    def test_track_danceability(self):
        self.assertEqual(self.test_track.danceability , self.mock.danceability)

    def test_track_energy(self):
        self.assertEqual(self.test_track.energy , self.mock.energy)