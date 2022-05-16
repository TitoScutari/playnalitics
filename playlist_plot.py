import plotly.graph_objects as go
from playnaliticsDB import playnaliticsDB

class PlaylistPlot():

  def __init__(self, playlist_id) -> None:
    self.__categories = ['acousticness', 'danceability', 'energy', 'valence', 'loudness']
    self.__fig = go.Figure()
    self.__playlist_id = playlist_id
    self.__db = playnaliticsDB()

  @property
  def categories(self):
    return self.__categories

  @property
  def fig(self):
    return self.__fig
  
  @property
  def playlist_id(self):
    return self.__playlist_id
  
  @property
  def db(self):
    return self.__db
  
  @property
  def list(self):
    return self.__list
  
  def load_playlist_data(self):
    self.db.connect()
    self.__list = self.db.select_playlist_tracks(self.playlist_id)
    self.db.close()
  
  def plot(self):
    for item in self.list:
      self.fig.add_trace(go.Scatterpolar(
            r=item[3:8],
            theta=self.categories,
            name=item[1]
      ))

    self.fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
          range=[0, 1]
        )),
      showlegend=True
    )

    self.fig.write_html('plot.html')