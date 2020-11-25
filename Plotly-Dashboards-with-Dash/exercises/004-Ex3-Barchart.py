#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# create a DataFrame from the .csv file:

df = pd.read_csv('~/PycharmProjects/Udemy-notebook/Plotly-Dashboards-with-Dash/Data/mocksurvey.csv', index_col=0)

# df1 = pd.DataFrame(['a', 'b', 'c', 'd', 'e'])
# df1.columns = df1.iloc[0]  # Use the first row as new header
# df1 = df1[1:]


# create traces using a list comprehension:
# create a layout, remember to set the barmode here
# create a fig from data & layout, and plot the fig.

data = [go.Bar(x=df.index, y=df[response], name=response) for response in df.columns]

layout = go.Layout(title='Mock Survey', barmode='stack')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)



# one line code for loops:
for i in range(10):
    if i < 5:
        j = i ** 2
    else:
        j = 0
    print(j)

for i in range(10): print(i ** 2 if i < 5 else 0)
