import plotly.plotly as plt
import plotly.graph_objs as gp
import numpy as np
import plotly
plotly.tools.set_credentials_file(username='belifakbar',api_key='tgEwd6FJbmHuWkRpHNxI')

N=100
x_random=np.random.randn(N)
y_random=np.random.randn(N)

trace0=gp.Scatter(
    x=x_random,
    y=y_random+2,
    name='Trace0',
    mode='markers',
    marker=dict(
        size=10,
        color='rgba(152,0,0,.8)',
        line=dict(width=2,color='rgb(0,0,0)'
                  )
    )
)
trace1=gp.Scatter(
    x=x_random,
    y=y_random-2,
    name='Trace1',
    mode='markers',
    marker=dict(
        size=10,
        color='rgba(255,182,193,.9)',
        line=dict(
            width=2,
        )
    )
)

data=[trace0,trace1]
plt.plot(data,filename='style-scatter')
