import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(x=random_x,
                   y=random_y,
                   mode='markers',
                   marker=dict(
                       size=15,
                       color='rgb(300,200,100)',
                       symbol='point',
                       line={'width': 2}
                   ))]

layout = go.Layout(title='This is a plot',
                   xaxis={'title': 'X Axis'},  # one way to display axis name
                   yaxis=dict(title='Y Axis'),  # another way to display axis name
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter.html')
