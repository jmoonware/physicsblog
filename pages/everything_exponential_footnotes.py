import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import logging
import glob
import settings,os

dash.register_page(__name__,title="John the Physicist")

layout = html.Div([
	dbc.Row([
		dcc.Markdown(r"1. Some restrictions may apply. Of course, we are talking about simple particle systems with elastic collisions. All bets are off in systems that react with one another (like, suddenly oxidizing a hydrocarbon gas) or systems with very large (relativistic) sizes, like galaxies.",mathjax=True), 
		], 
		justify='center'),
])
