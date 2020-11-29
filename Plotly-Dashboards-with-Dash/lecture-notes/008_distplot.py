import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

x = np.random.randn(1000)

hist_data = [x]
group_labels = ['distplot']

fig = ff.create_distplot(hist_data=hist_data, group_labels=group_labels)

pyo.plot(fig)


x1 = np.random.randn(200)-2
x2 = np.random.randn(200)
x3 = np.random.randn(200)+2
x4 = np.random.randn(200)+4

hist_data2 = [x1, x2, x3, x4]
group_labels2 = ['x1', 'x2', 'x3', 'x4']

fig2 = ff.create_distplot(hist_data=hist_data2, group_labels=group_labels2)
pyo.plot(fig2)

