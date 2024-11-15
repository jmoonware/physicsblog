import dash
from dash import dcc, html, callback, Input, Output, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objects as go 
import numpy as np
import random
import logging
import pandas as pd

try:
	dash.register_page(__name__,title="John the Physicist")
			
	layout = html.Div([
		dbc.Row([
			dbc.CardGroup([
				dbc.Card([
					html.H4('Navigation Table',style={'text-align':'center'}),
					html.Div(dbc.Button("Search",id='search_button')),			
					html.Div(dash_table.DataTable(id='toc_table'),id='table_div'),			
				]),
			]),
		],justify='center')
	
	])
	
	@callback(
		Output(component_id='table_div', component_property='children'),
		Input(component_id='search_button', component_property='n_clicks'),
		)
	def update_toc_table(*args):
		logging.getLogger(__name__).info("Callbark xxx")
		N = 100
		df = pd.DataFrame({
			'Coin':[i for i in range(N)],
			'Left a':[np.random.rand() for _ in range(N)],
			'Left b':[np.random.rand() for _ in range(N)],
			'Left c':[np.random.rand() for _ in range(N)],
		})
		return dash_table.DataTable(df.to_dict('records'))

except Exception as ex:
	logging.getLogger(__name__).error(__name__+" : Last chance exception:"+str(ex))
	logging.getLogger(__name__).info(__name__+" : Exit on last-chance exception")
finally:
	logging.getLogger(__name__).info(__name__+" : Reached finally OK")
