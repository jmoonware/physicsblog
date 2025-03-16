import dash
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
import logging
import mdutil

try:
	dash.register_page(__name__,title="John the Physicist")
	
	pmd = []
	mdutil.build_markdown(__name__,"start_post","Figure1","assets/Fig1_quantum_logic.png",pmd)
	mdutil.build_markdown(__name__,"Figure1","Figure2","assets/Fig2_quantum_logic.png",pmd,width=500)
	mdutil.build_markdown(__name__,"Figure2","Figure3","assets/Fig3_quantum_logic.png",pmd)
	mdutil.build_markdown(__name__,"Figure3","Figure4","assets/Fig4_quantum_logic.png",pmd)
	mdutil.build_markdown(__name__,"Figure4","Figure5","assets/Fig5_quantum_logic.png",pmd)
	mdutil.build_markdown(__name__,"Figure5","Figure6","assets/Fig6_quantum_logic.png",pmd)
	mdutil.build_markdown(__name__,"Figure6","Figure7","assets/Fig7_quantum_logic.png",pmd)
	mdutil.build_markdown(__name__,"Figure7","Figure8","assets/Fig8_quantum_logic.png",pmd,width=500)
	mdutil.build_markdown(__name__,"Figure8","Figure9","assets/Fig9_quantum_logic.png",pmd,width=500)
	mdutil.build_markdown(__name__,"Figure9","Figure10","assets/Fig10_quantum_logic.png",pmd)
	mdutil.build_markdown(__name__,"Figure10","Figure11","assets/Fig11_quantum_logic.png",pmd)
	mdutil.build_markdown(__name__,"Figure11","Figure12","assets/Fig12_quantum_logic.png",pmd)
	mdutil.build_markdown(__name__,"Figure12","Figure13","assets/Fig13_quantum_logic.png",pmd)
	mdutil.build_markdown(__name__,"Figure13","Figure14","assets/Fig14_quantum_logic.png",pmd)
	mdutil.build_markdown(__name__,"Figure14","Figure15","assets/Fig15_quantum_logic.png",pmd)
	mdutil.build_markdown(__name__,"Figure15","Figure16","assets/Fig16_quantum_logic.png",pmd)
	mdutil.build_markdown(__name__,"Figure16","Figure17","assets/Fig17_quantum_logic.png",pmd)
	mdutil.build_markdown(__name__,"Figure17","",None,pmd)
	
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
