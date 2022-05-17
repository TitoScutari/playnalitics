from playlist_plot import PlaylistPlot
import sys

def main(id_):
    plotter = PlaylistPlot(id_)
    plotter.load_playlist_data()
    plotter.plot()

if __name__ == "__main__":
    playlist_id = sys.argv[1]
    with open("log_on_plylist.log", 'a') as file:
        file.write(playlist_id)
        file.close()
    main(playlist_id)
    