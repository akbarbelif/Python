import plotly.plotly as pl
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='belifakbar',api_key='tgEwd6FJbmHuWkRpHNxI')
import numpy as np

N=100
random_x=np.linspace(0,1,N)
random_y0 = np.random.randn(N)+5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N)-5


# Create traces
trace0 = go.Scatter(
    x = random_x,
    y = random_y0,
    mode = 'markers',
    name = 'Scatter'
)
# trace1 = go.Scatter(
#     x = random_x,
#     y = random_y1,
#     mode = 'lines+markers',
#     name = 'lines+markers'
# )
trace2 = go.Scatter(
    x = random_x,
    y = random_y2,
    mode = 'lines',
    name = 'lines'
)

data = [trace0, trace2]
pl.plot(data, filename='scatter-mode')

# # Create traces Scatter
# trace_scatter=go.Scatter(
#     x=x_rand_scatter,
#     y=y_rand_scatter,
#     mode='makers',
#     name='makers')
# #Create Trace Lines
# trace_line=go.Scatter(
#     x=x_rand_line,
#     y=y_rand_line,
#     mode='lines',
#     name='lines')
# #data = [trace_scatter,trace_line]
# #pl.plot(data)
