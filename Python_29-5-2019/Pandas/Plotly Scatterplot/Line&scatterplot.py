import plotly.plotly as pl
import plotly.graph_objs as go
import numpy as np

N=100
x_rand_scatter=np.random.randn(N)
y_rand_scatter=np.random.randn(N)

x_rand_line=np.random.randn(N)
y_rand_line=np.random.randn(N)

trace_scatter=go.Scatter(x=x_rand_scatter,y=y_rand_scatter)
trace_line=go.Scatter(x=x_rand_line,y=y_rand_line)
data=[trace_scatter,trace_line]
pl.plot(data)
