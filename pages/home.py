import dash
import dash_bootstrap_components as dbc
from dash import html, Input, Output, State, ctx, dcc
from flask import request, Response, make_response
import flask
from dash.exceptions import PreventUpdate
import logging
import dash_player as dp

# start last-chance exception block
try:

	dash.register_page(__name__,title="John the Physicist", path='/')

	fp_anim = "assets/test.mp4"

	# Layout
	layout=[]
	layout.append(
		dbc.Row([
			dp.DashPlayer(
				url=fp_anim,
				playing=True,
				loop=True,
				muted=True,
				playsinline=True,
				width='100%',
			),

#			dbc.CardGroup([
#		        dbc.Card([
#					dbc.CardBody([
#						dcc.Markdown("$$e^{i\\pi}+1=0$$",mathjax=True),
#						html.H4("Welcome",className='card-title'),
#						html.P("Recent Posts",className="text-primary"),
#					]),
#				]),
#			],style={'width':'95%'}),
		],justify='center',style={'margin-top':5})
	)

#	layout.append(
#		dbc.Row([
#			dbc.CardGroup([
#		        dbc.Card([
#					dbc.CardBody([
#						html.H5("Contact",className='card-title',id='contact'),
#						html.Br(),
#						html.Div("Someplace USA",className="text-primary"),
#						dbc.CardLink("someone@gmail.com",href="mailto:someone@gmail.com"),
#					]),
#				],color='light'),
#			],style={'width':'95%'}),
#		],justify='center',style={'margin-top':5})
#	)
	# final credits
	layout.append(
		html.Div("Built with Dash and Plotly",style={'color':'grey','text-align':'center','font-size':'0.75em'})
	)

except Exception as ex:
	logging.getLogger(__name__).error(__name__ + ": Last chance exception:"+str(ex))
	logging.getLogger(__name__).info(__name__ + ": Exit on last-chance exception")
finally:
	logging.getLogger(__name__).info(__name__ + ": Reached finally OK")
