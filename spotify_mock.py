class SpotifyMock:

    def __init__(self) -> None:
        pass

    @property
    def user_ID(self):
        return '1167306845'
    
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
    