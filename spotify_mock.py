class SpotifyMock:

    def __init__(self) -> None:
        pass

    @property
    def user_ID(self):
        return '1167306845'

    @property
    def user_name(self):
        return 'Tito Scutari'
    
    @property
    def playlist_ID(self):
        return '1Nsa36wMAco0no4fGEiKsy'
    
    @property
    def playlist_owner(self):
        return self.user_ID

    @property
    def playlist_name(self):
        return 'test'
    
    @property
    def track_ID(self):
        return '6UB9mShVLbMm0W4e6vud4C'

    #TODO
    @property
    def title(self):
        return "Battery"
    
    @property
    def artist(self):
        return "Metallica"
    
    @property
    def key(self):
        return 11
    
    @property
    def bpm(self):
        return 96.699
    
    @property
    def valence(self):
        return 0.427
    
    @property
    def loudness(self):
        return -8.799
    
    @property
    def acousticness(self):
        return 0.00022
    
    @property
    def danceability(self):
        return 0.481
    
    @property
    def energy(self):
        return 0.928
    