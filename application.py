import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
# Beanstalk looks for application by default, if this isn't set you will get a WSGI error.
application = app.server

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        This is Dash running on Elastic Beanstalk.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [0, 6, 0], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [6, 6, 6], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash testing Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    # Beanstalk expects it to be running on 8080.
    application.run(debug=True, port=8080)
