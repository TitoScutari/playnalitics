import pandas as pd
import numpy as np
import plotly.graph_objects as go

# TODO import data from json to pandas dataframe

categories = ['acousticness', 'danceability', 'energy', 'valence', 'loudness']
fig = go.Figure()

# TODO looping on tracks, accessing dataframe
fig.add_trace(go.Scatterpolar(
      r=[0.1, 0.5, 0.7, 0.2, 0.3,0.1],
      theta=categories,
      name='song1'
))
fig.add_trace(go.Scatterpolar(
      r=[0.4, 0.3, 0.5, 0.8, 0.2,0.4],
      theta=categories,
      name='song2'
))

# OUTPUT
fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 1]
    )),
  showlegend=True
)

fig.write_html('plot.html')