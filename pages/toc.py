import dash
from dash import dcc, html, callback, Input, Output, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objects as go 
import numpy as np
import random
import logging
import pandas as pd 
import tocutil

try:
	dash.register_page(__name__,title="John the Physicist")

	tocutil.update('pages')

	layout = [
		dbc.Row(
			dbc.Card(
				dbc.CardBody(
					dbc.Accordion([
						dbc.AccordionItem([
							html.H4('Navigation Table',style={'text-align':'center'}),
							html.Div("Sort by"),
							html.Div(dcc.Dropdown(tocutil.get_sortitems(),multi=True,id='sort_dropdown')),
							html.Div("Filter by topic"),
							html.Div(dcc.Dropdown(tocutil.get_topics(),multi=True,id='topic_dropdown')),
							html.Div(dbc.Button("Search",id='search_button')),
						],title="Navigation"),
						],
						start_collapsed=True,
					),
				),
				outline=False,
			),
		),			
		dbc.Row(
			html.Div(id = 'toc_cards'),
			style={'padding-right':'2%','margin-top':'2%','padding-left':'2%'},
		),
	]

	
	@callback(
		Output(component_id='toc_cards', component_property='children'),
		[
			Input(component_id='search_button', component_property='n_clicks'),
			Input(component_id='topic_dropdown', component_property='value'),
		],
		)
	def update_toc_table(*args):
		nclk = args[0]
		dd_val = args[1]
		logging.getLogger(__name__).info(str((nclk, dd_val)))
		recs = tocutil.get_recs(dd_val)
		cards = []
		for r in recs:
			cards.append(
				dbc.Card([
					dbc.CardHeader(r.date),
					dbc.CardBody([
						html.H4(r.title),
						html.P(r.description),
						dbc.CardLink("Read...",href=dash.page_registry[r.location]['path']),
						dbc.Accordion([
							dbc.AccordionItem([
								html.Span([
									"Order ",
									dbc.Badge("{0}".format(r.logical_order)), 
									" Level ",
									dbc.Badge("{0}".format(r.difficulty)),
									" Topics ",
									dbc.Badge("{0}".format(', '.join(r.topics))),
								]),
								],title="Info"),
							],start_collapsed=True,
						),
					]),
				],outline=False)
			)
		return cards

except Exception as ex:
	logging.getLogger(__name__).error(__name__+" : Last chance exception:"+str(ex))
	logging.getLogger(__name__).info(__name__+" : Exit on last-chance exception")
finally:
	logging.getLogger(__name__).info(__name__+" : Reached finally OK")
