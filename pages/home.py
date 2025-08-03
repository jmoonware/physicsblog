import dash
import dash_bootstrap_components as dbc
from dash import html, Input, Output, State, ctx, dcc
from flask import request, Response, make_response
import flask
from dash.exceptions import PreventUpdate
import logging
# import dash_player as dp

# start last-chance exception block
try:

	dash.register_page(__name__,title="John the Physicist", path='/')

	fp_anim = "assets/test.mp4"
	front_image="assets/paradown.jpg"

	# Layout
	layout=[]
	layout.append(
		dbc.Row([
#			dp.DashPlayer(
#				url=fp_anim,
#				playing=True,
#				loop=True,
#				muted=True,
#				playsinline=True,
#				width='100%',
#			),
			html.Img(src=front_image), # width=500),
		],justify='center',style={'margin-top':5})
	)

	layout.append(
		dbc.Row([
			html.Br(),
			html.H3("\"It is what it does.\"",style={'text-align':'center'}),
			html.Br(),
			html.Div("Reflections on physics, mathematics, finance, and anything else that I find interesting.",style={'text-align':'center'}),
		],justify='center',style={'margin-top':5})
	)

	layout.append(html.Br())

	# final credits
	layout.append(
		html.Div("Built with Dash and Plotly",style={'color':'grey','text-align':'center','font-size':'0.5em'})
	)

except Exception as ex:
	logging.getLogger(__name__).error(__name__ + ": Last chance exception:"+str(ex))
	logging.getLogger(__name__).info(__name__ + ": Exit on last-chance exception")
finally:
	logging.getLogger(__name__).info(__name__ + ": Reached finally OK")
