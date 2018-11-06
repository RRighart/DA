import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
application = app.server

#df = pd.DataFrame({'X':[1,2,3,4,5], 'Y':[1,3,9,16,27], 'Name':['A', 'B', 'C', 'D', 'E']})

#df.to_csv('example_df.csv', index=False, header=True)
#df = pd.read_csv('example_df.csv')

#print(df.head())

#app.layout = html.Div([
#    dcc.Graph(
#        id='Test X-Y',
#        figure={
#            'data': [
#                go.Scatter(
#                    x=df['X'],
#                    y=df['Y'],
#                    text=df['Name'],
#                    mode='markers',
#                    opacity=0.7,
#                    marker={
#                        'size': 15,
#                        'line': {'width': 0.5, 'color': 'white'}}
#                    )        
#            ],
#
#            'layout': go.Layout(
#                xaxis={'title': 'X-Axis'},
#                yaxis={'title': 'Y-Axis'},
#                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
#                legend={'x': 0, 'y': 1},
#                hovermode='closest')
#        }
#    )
#])

if __name__ == '__main__':
    application.run(debug=True, port=8080)
