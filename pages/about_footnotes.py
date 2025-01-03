import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__,title="John the Physicist")

layout = html.Div([
	dbc.Row([
		dcc.Markdown(" 1. The JTP name is a play on 'John the Baptist', suggested by my friend and cycling buddy Steve during one of our meandering conversations about religion and science."),
		], justify='center'),
])
