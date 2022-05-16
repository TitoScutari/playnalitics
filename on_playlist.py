from playlist_plot import PlaylistPlot
from spotify_mock import SpotifyMock
import sys

def main(playlist_id):
    plotter = PlaylistPlot(playlist_id)
    plotter.load_playlist_data()
    plotter.plot()

if __name__ == "__main__":
    playlist_id = sys.argv[1]
    main(playlist_id)