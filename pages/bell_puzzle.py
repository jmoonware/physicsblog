import dash
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go 
import numpy as np
import random
import logging
import mdutil
import bellcalcs

def build_sim_layout():
	els = [
		html.P(" "),	
		dcc.Graph(id='bell_graph_trials'),	
		dbc.Stack([	
			dbc.Row([
				dbc.Col(dcc.Markdown("Bias &#x25D1"),width={'size':2,'offset':1},align='center'),
				dbc.Col(dcc.Slider(min=0, max=bias_range, step=1, value=bias_range/2,id='bell_slider_bias_ball',marks=bias_marks),width={'size':9},align='center'),
			],align='center'),	
			dbc.Row([
				dbc.Col(dcc.Markdown("Bias &#x25E8"),width={'size':2,'offset':1},align='center'),
				dbc.Col(dcc.Slider(min=0, max=bias_range, step=1, value=bias_range/2,id='bell_slider_bias_cube',marks=bias_marks),width={'size':9},align='center'),
			],align='center'),	
			dbc.Row([
				dbc.Col(dcc.Markdown("Bias &#x25EE"),width={'size':2,'offset':1},align='center'),
				dbc.Col(dcc.Slider(min=0, max=bias_range, step=1, value=bias_range/2,id='bell_slider_bias_tri',marks=bias_marks),width={'size':9},align='center'),
			],align='center'),	
	
			dbc.Row([
				dbc.Col(dbc.Label("Coins"),width={'size':1,'offset':1},align='center'),
				dbc.Col(dbc.Input(type="number", min=3, max=1000, step=1, value=100,id='bell_two_coins'),width={'size':6,'offset':1},align='center'),			
			],align='center'),			
			dbc.Row([
				dbc.Col(dbc.Label("Trials"),width={'size':1,'offset':1},align='center'),
				dbc.Col(dbc.Input(type="number", min=1, max=100, step=1, value=50,id='bell_two_trials'),width={'size':6,'offset':1},align='center'),			
			],align='center'),
			dbc.Row([
				dbc.Col(dcc.Markdown("LR-X &#x25D1,&#x25E8"),width={'size':2,'offset':1},align='center'),
				dbc.Col(dcc.Slider(min=0, max=bias_range, step=1, value=0,id='bell_slider_bc_lrx',marks=bias_marks),width={'size':9},align='center'),
			],align='center'),	
		],gap=3),		
		html.P(" "),	
	]
	return(dbc.Card(els))

try:
	dash.register_page(__name__,title="John the Physicist")

	bias_marks={}
	bias_range=10
	for i in range(bias_range+1):
		bias_marks[i]="{0:.1f}".format(float(i)/bias_range)
	
	pmd = []
	mdutil.build_markdown(__name__,"start_post","Figure1","assets/bell_vending_one.png",pmd)
	mdutil.build_markdown(__name__,"Figure1","Figure2","assets/one_pair_venn.png",pmd)
	mdutil.build_markdown(__name__,"Figure2","Figure3","assets/bell_vending_two.png",pmd)
	mdutil.build_markdown(__name__,"Figure3","Figure4","assets/two_pair_venn.png",pmd)
	mdutil.build_markdown(__name__,"Figure4","Figure5","assets/two_pair_b1.png",pmd)
	mdutil.build_markdown(__name__,"Figure5","Figure6","assets/two_pair_b2.png",pmd)
	mdutil.build_markdown(__name__,"Figure6","Figure7","assets/bell_vending_three.png",pmd)
	mdutil.build_markdown(__name__,"Figure7","Figure8","assets/three_pair_venn.png",pmd)
	mdutil.build_markdown(__name__,"Figure8","Figure9","assets/three_pair_venn_b1.png",pmd)
	mdutil.build_markdown(__name__,"Figure9","Figure10","assets/three_pair_venn_b2.png",pmd)
	mdutil.build_markdown(__name__,"Figure10","Figure11","assets/three_pair_venn_b3.png",pmd)
	mdutil.build_markdown(__name__,"Figure11","Figure12","assets/bell_boundary.png",pmd)
	mdutil.build_markdown(__name__,"Figure12","three_shape_simulator",None,pmd)
	pmd.append(build_sim_layout())
	mdutil.build_markdown(__name__,"three_shape_simulator","Figure13","assets/bell_violation_stats.png",pmd)
	mdutil.build_markdown(__name__,"Figure13","Figure14","assets/bell_violation_stats_x.png",pmd)
	mdutil.build_markdown(__name__,"Figure14","",None,pmd)
	
	layout = html.Div([
		dbc.Row([
			dbc.CardGroup([
				dbc.Card([
					dbc.CardBody(pmd),
				]),
			]),
		],justify='center'),
	])
	
	@callback(
		Output(component_id='bell_graph_trials', component_property='figure'),
		[
		Input(component_id='bell_slider_bias_ball', component_property='value'),
		Input(component_id='bell_slider_bias_cube', component_property='value'),
		Input(component_id='bell_slider_bias_tri', component_property='value'),
		Input(component_id='bell_two_coins', component_property='value'),
		Input(component_id='bell_two_trials', component_property='value'),
		Input(component_id='bell_slider_bc_lrx', component_property='value'),
		]
	)
	def update_bell_graph(*args):
		bias_ball = args[0]/bias_range
		bias_cube = args[1]/bias_range
		bias_tri = args[2]/bias_range
		ncoin = args[3]
		ntrial = args[4]
		bc_lrx = args[5]/bias_range
		logging.getLogger(__name__).info(__name__+" **** Bell slider {0} {1} {2}".format(bias_ball,ncoin,ntrial))
		# callback gives NoneType sometimes
		if bias_ball and bias_cube and bias_tri and ncoin and ntrial:
			be_l,be_r = bellcalcs.gen_bell_stats(ntrial,ncoin,b_bias=bias_ball,c_bias=bias_cube,t_bias=bias_tri,bc_lrx=bc_lrx)
			x = np.array([i+1 for i in range(len(be_l))])
			fig_trials = go.Figure()
			fig_trials.add_traces([
				go.Scattergl(x=x,y=be_l,mode='markers',name="N(bw,cw)"),
				go.Scattergl(x=x,y=be_r,mode='markers',name="N(bw,tw)+N(tw,cw)"),
			])
			# mark failures
			f = be_l > be_r
			if sum(f) > 0: # found a failure
				xf = x[f]
				yf = be_l[f]*1.05
				fig_trials.add_trace(
					go.Scattergl(x=xf,y=yf,mode='markers',name="Violation",
					marker=dict(color='red',size=10))
				)	
			fig_trials.update_layout(plot_bgcolor='#010103',
				template='simple_white',
				showlegend=True,
				height=300,
				legend=dict(x=0.05,y=0.95),
				margin=dict(l=0, r=0, t=0, b=0.1),
				xaxis=dict(title=dict(text="Trial")),
				yaxis=dict(title=dict(text="Observations")),
			)
		else:
			raise Exception("Unusable value - None") # this is the recommended solution
	
		return fig_trials

except Exception as ex:
	logging.getLogger(__name__).error(__name__+" : Last chance exception:"+str(ex))
	logging.getLogger(__name__).info(__name__+" : Exit on last-chance exception")
finally:
	logging.getLogger(__name__).info(__name__+" : Reached finally OK")
