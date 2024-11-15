import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__,title="John the Physicist")

layout = html.Div([
	dbc.Row([
		dbc.CardGroup([
			dbc.Card([
				dbc.CardBody([
					html.H4('About John the Physicist',style={'text-align':'center'}),
					dcc.Markdown(
"Some stuff in markdown."
					),
					html.A(html.Img(src='assets/In-Blue-34.png'),href="https://www.linkedin.com/in/john-a-moon-physics"),
				])
			])
		]),
	],justify='center')
])
