import dash
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
import logging
import mdutil

try:
	dash.register_page(__name__,title="John the Physicist")
	
	pmd = []
	mdutil.build_markdown(__name__,"start_post","Figure1","assets/Fig1_quantum_warmup.png",pmd,width=400)
	mdutil.build_markdown(__name__,"Figure1","Figure2","assets/Fig2_quantum_warmup.png",pmd,width=400)
	mdutil.build_markdown(__name__,"Figure2","Figure3","assets/Fig3_quantum_warmup.png",pmd)
	mdutil.build_markdown(__name__,"Figure3","Figure4","assets/Fig4_quantum_warmup.png",pmd)
	mdutil.build_markdown(__name__,"Figure4","Figure5","assets/Fig5_quantum_warmup.png",pmd)
	mdutil.build_markdown(__name__,"Figure5","Figure6","assets/Fig6_quantum_warmup.png",pmd)
	mdutil.build_markdown(__name__,"Figure6","",None,pmd)
	
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
