import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.plotly as pl
import matplotlib.pyplot as plt

N=1000
x_rand=np.random.randn(N)
y_rand=np.random.randn(N)

trace=go.Scatter(x=x_rand,y=y_rand,mode='markers')
data=[trace]

pl.plot(data,filename='basic-scatter')

#pl.iplot(data)
