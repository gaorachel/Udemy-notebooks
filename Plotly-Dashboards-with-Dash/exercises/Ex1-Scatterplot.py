#######
# Objective: Create a scatterplot of 1000 random data points.
# x-axis values should come from a normal distribution using
# np.random.randn(1000)
# y-axis values should come from a uniform distribution over [0,1) using
# np.random.rand(1000)
######

# Perform imports here:
# Define a data variable
# Define the layout
# Create a fig from data and layout, and plot the fig

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

random_x = np.random.randn(1000)
random_y = np.random.rand(1000)

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
                   xaxis=dict(title='X Axis'),  # one way to display axis name
                   yaxis=dict(title='Y Axis'),  # another way to display axis name
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter-exercises.html')
