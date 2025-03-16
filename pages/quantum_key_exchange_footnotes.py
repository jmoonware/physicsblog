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
		dcc.Markdown(r"1. By the way, we could also use an entanglement generator that sends 'HV,VH' pairs (as we did in the post on [Bell's Inequality](bell-predictions)) which changes the correlation function to a sine. But since we have been talking about quantum computing so much (where $H\rightarrow 0$ and $V \rightarrow 1$), let's use the symmetric cosine form for communications.",mathjax=True), 
		], 		
		justify='center'),
])
