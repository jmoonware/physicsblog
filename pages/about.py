import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import mdutil
import os
import logging

dash.register_page(__name__,title="John the Physicist")

layout = html.Div([
	dbc.Row([
		dbc.CardGroup([
			dbc.Card([
				dbc.CardBody([
					dcc.Markdown(
						mdutil.get_section(__name__), mathjax=True,
					),
					html.A(html.Img(src='assets/In-Blue-34.png'),href="https://www.linkedin.com/in/john-a-moon-physics"),
				])
			])
		]),
	],justify='center')
])
