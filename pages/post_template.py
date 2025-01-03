import dash
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go 
import numpy as np
import random
import logging

try:
	dash.register_page(__name__,title="John the Physicist")
			
	layout = html.Div([
		dbc.Row([
			dbc.CardGroup([
				dbc.Card([
					dbc.CardBody([
						html.H4('Post Title',style={'text-align':'center'}),
						dcc.Markdown(
	"Some stuff in markdown. An in-line equation ${\\phi} = {0}$",mathjax=True
						),
						dcc.Markdown(
	"$$\\left|{\\phi}\\right> = \\left|{0}\\right>$$",mathjax=True
						),
					])
				]),
				dbc.Card([
					html.Div(dcc.Graph(id='example-graph')),			
					html.Div(dcc.Slider(min=0, max=20, step=5, value=10,id='example-slider')),			
				]),
			]),
		],justify='center')
	
	])
	
	@callback(
		Output(component_id='example-graph', component_property='figure'),
		[
			Input(component_id='example-slider', component_property='value'),
		]
		)
	def update_data_graph(*args):
		logging.getLogger(__name__).info("**** Callback slider")
		fig = go.Figure(
			go.Scattergl(x=np.random.randn(1000),
			y=np.random.randn(1000),
			mode='markers',
			marker=dict(
				color=random.sample(['#ecf0f1'] * 500 +
				["#3498db"] * 500, 1000),
			line_width=1)
		))
		fig.update_layout(plot_bgcolor='#010103',
#			width=790,
#			height=730,
			xaxis_visible=False,
			yaxis_visible=False,
			showlegend=False,
			margin=dict(l=0, r=0, t=0, b=0))
		return fig

except Exception as ex:
	logging.getLogger(__name__).error(__name__+" : Last chance exception:"+str(ex))
	logging.getLogger(__name__).info(__name__+" : Exit on last-chance exception")
finally:
	logging.getLogger(__name__).info(__name__+" : Reached finally OK")
