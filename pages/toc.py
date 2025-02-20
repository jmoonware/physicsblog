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
							html.H5("Sort by"),
							html.Div(dcc.Dropdown(tocutil.get_sortitems(),multi=True,id='sort_dropdown')),
							html.Div(dcc.Checklist([" Ascending"],id='sort_check')),
							html.H5("Filter by topic"),
							html.Div(dcc.Dropdown(tocutil.get_topics(),multi=True,id='topic_dropdown')),
#							html.Div(dbc.Button("Search",id='search_button')),
							html.Div(dbc.CardLink("Summary Page",href='summary')),
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
#			Input(component_id='search_button', component_property='n_clicks'),
			Input(component_id='topic_dropdown', component_property='value'),
			Input(component_id='sort_dropdown', component_property='value'),
			Input(component_id='sort_check', component_property='value'),
		],
		)
	def update_toc_table(*args):
#		nclk = args[0]
		topic_dd_val = args[0]
		sort_dd_val = args[1]
		if args[2]!=None and len(args[2])>0:
			sort_ascend=True
		else:
			sort_ascend=False
#		logging.getLogger(__name__).info(str((nclk, topic_dd_val,sort_ascend)))
#		logging.getLogger(__name__).info(str((topic_dd_val,sort_ascend)))
		recs = tocutil.get_recs(topic_dd_val,sort_dd_val,sort_ascend)
		cards = []
		for r in recs:
			cards.append(
				dbc.Card([
					dbc.CardHeader(r.date_iso),
					dbc.CardBody([
						html.H4(r.title),
						html.P(r.description),
						dbc.CardLink("Read...",href=dash.page_registry[r.location]['path']),
						dbc.Accordion([
							dbc.AccordionItem([
								html.Span([
									"Order ",
									dbc.Badge("{0}".format(r.logical)), 
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
