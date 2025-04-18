import dash
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
import logging
import mdutil

try:
	dash.register_page(__name__,title="John the Physicist")
	
	pmd = []
	mdutil.build_markdown(__name__,"start_post","Figure1","assets/Fig1_listening_to_integers.png",pmd,width=500)
	mdutil.build_markdown(__name__,"Figure1","Figure2","assets/Fig2_listening_to_integers.png",pmd,width=600)
	mdutil.build_markdown(__name__,"Figure2","Figure3","assets/Fig3_listening_to_integers.png",pmd)
	mdutil.build_markdown(__name__,"Figure3","",None,pmd)
	
	layout = html.Div([
		dbc.Row([
			dbc.CardGroup([
				dbc.Card([
					dbc.CardBody(pmd),
				]),
			]),
		],justify='center'),
	])

except Exception as ex:
	logging.getLogger(__name__).error(__name__+" : Last chance exception:"+str(ex))
	logging.getLogger(__name__).info(__name__+" : Exit on last-chance exception")
finally:
	logging.getLogger(__name__).info(__name__+" : Reached finally OK")
