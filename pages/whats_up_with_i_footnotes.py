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
		dcc.Markdown(r"1. We are going to use the '-' sign in the exponent because we want travelling waves to appear to move in the positive direction when time changes a positive amount. It's a subtle but important point, as both sign conventions 'work', but the negative time exponent is the accepted convention.",mathjax=True), 
		], 
		justify='center'),
])
