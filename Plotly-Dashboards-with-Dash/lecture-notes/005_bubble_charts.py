import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('~/PycharmProjects/Udemy-notebook/Plotly-Dashboards-with-Dash/Data/mpg.csv')
print(df)
print(df.columns)
print(df.index)

data = [go.Scatter(x=df['horsepower'],
                   y=df['mpg'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=df['weight']/100,
                               color=df['cylinders'],
                               showscale=True))]

layout = go.Layout(title='Bubble Chart', hovermode='x')  # hovermode='x/y/clusest'
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)