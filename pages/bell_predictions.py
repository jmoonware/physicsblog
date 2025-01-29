import dash
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go 
import numpy as np
import random
import logging
import mdutil
import bellcalcs
import plotly.graph_objects as go
from scipy.special import erf


tmax = 0.5 # ps
zmax = 150 # um
d_cryst = 5 # um

zoom=[0.25,.5,1,2,3,4]
zoom_labels = ["{0:.1f}".format(x) for x in zoom]
zoom_marks={}
for ix,x in enumerate(zoom_labels):
	zoom_marks[ix]=x

check_items=['  Annotations','  Axis Labels']

def build_sim_layout():
	els = [
		html.P(" "),	
		dcc.Graph(id='bell_graph_pol',config={'displaylogo':False,'showTips':False}),
		html.P(" "),	
		dbc.Stack([	
			dbc.Row([
				dbc.Col(dcc.Markdown("Time ($\\tau$, ps)",mathjax=True),width={'size':2,'offset':1},align='center'),
				dbc.Col(dcc.Slider(min=-tmax, max=tmax, step=int(2*tmax/10), value=0,id='bell_time'),width={'size':9},align='center'),
			],align='center'),	
			dbc.Row([
				dbc.Col(dcc.Markdown("Rot (deg)"),width={'size':2,'offset':1},align='center'),
				dbc.Col(dcc.Slider(min=0, max=180, step=22.5, value=22.5,id='bell_rot'),width={'size':9},align='center'),
			],align='center'),	
			dbc.Row([
				dbc.Col(dcc.Markdown("Zoom (x)"),width={'size':2,'offset':1},align='center'),
				dbc.Col(dcc.Slider(min=0, max=len(zoom)-1, step=1, value=2,id='bell_zoom',marks=zoom_marks),width={'size':9},align='center'),
			],align='center'),	
		],gap=3),		
			dbc.Row([
				dbc.Col(dcc.Checklist(check_items,id="bell_checklist"),width={'size':9,'offset':2},align='center'),
			],align='center'),	
		html.P(" "),	
	]
	return(dbc.Card(els))

try:
	dash.register_page(__name__,title="John the Physicist")

	bias_marks={}
	bias_range=10
	for i in range(1,bias_range+1):
		bias_marks[i]="{0:.1f}".format(float(i)/bias_range)
	
	pmd = []
	mdutil.build_markdown(__name__,"start_post","Figure1","",pmd)
	pmd.append(build_sim_layout())
	mdutil.build_markdown(__name__,"Figure1","Figure2","assets/bell_detector.png",pmd)
	mdutil.build_markdown(__name__,"Figure2","Figure3","assets/c_cor_bell.png",pmd,width=350)
	mdutil.build_markdown(__name__,"Figure3","Figure4","assets/q_c_correl.png",pmd)
	mdutil.build_markdown(__name__,"Figure4","Figure5","assets/q_cor_bell.png",pmd)
	mdutil.build_markdown(__name__,"Figure5","",None,pmd)
	
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
		Output(component_id='bell_graph_pol', component_property='figure'),
		[
		Input(component_id='bell_time', component_property='value'),
		Input(component_id='bell_rot', component_property='value'),
		Input(component_id='bell_zoom', component_property='value'),
		Input(component_id='bell_checklist', component_property='value'),
		]
	)
	def update_bell_pol(*args):
		td = args[0]
		if td==None:
			td=0
		yr = args[1]
		if yr==None:
			yr=0
		else:
			yr=yr*np.pi/180
		zm = args[2]
		if zm == None or zm < 0 or zm > len(zoom)-1:
			zm=1
		else:
			zm=zoom[int(zm)]
		chk = args[3]
		if chk==None:
			chk=[]
		logging.getLogger(__name__).error("td={0}, chk={1}".format(td,chk))
#		else:
#			raise Exception("Unusable value - None") 
		# update axes cones 
		axes = go.Cone(colorbar=None,sizemode='absolute',sizeref=0.3,showscale=False)
		axis_len = 0.1*zmax
		axes.x = [axis_len,0,0]
		axes.y = [0,axis_len,0]
		axes.z = [0,0,axis_len]
		axes.u = [1,0,0]
		axes.v = [0,1,0]
		axes.w = [0,0,1]
		
		pump_scatter = go.Scatter3d(name="Pump")
		sig_scatter = go.Scatter3d(name="Field L")
		idler_scatter = go.Scatter3d(name="Field R",marker=dict(color='red')) #,line=dict(dash='dot'))
		theta_si = 15 # degrees, half-angle
		c_si = np.cos(np.pi*theta_si/180)
		s_si = np.sin(np.pi*theta_si/180)
		fig = go.Figure()
		c = 300 # um/ps
		k = 2*3.142/0.4
		w = c*k
		dz = 0.1
		z = np.arange(-zmax,zmax+dz,dz)
		z0 = np.argmin(np.abs(z))
		tau=2*3.14*10 # cycles
		arg = k*z-w*td
		env = 0.5*(1-erf(2*z/d_cryst))

		pump_scatter.x=0.5*zmax*env*np.cos(arg)*np.exp(-(arg/tau)**2)
		pump_scatter.y=np.zeros(len(z))
		pump_scatter.z=z
		pump_scatter.mode='lines'
		fig.add_trace(pump_scatter)

		sig_scatter.x=(0.5*zmax)*(1-env[z0:])*np.cos(arg[z0:]/2)*np.exp(-(arg[z0:]/tau)**2)
		sig_scatter.y= z[z0:]*s_si
		sig_scatter.z=z[z0:]*c_si
		sig_scatter.mode='lines'
		fig.add_trace(sig_scatter)

		idler_scatter.y=(0.5*zmax)*(1-env[z0:])*np.cos(arg[z0:]/2)*np.exp(-(arg[z0:]/tau)**2)*c_si - z[z0:]*s_si
		idler_scatter.x=np.zeros(len(idler_scatter.y))
		idler_scatter.z=z[z0:]*c_si
		idler_scatter.mode='lines'
		fig.add_trace(idler_scatter)
		
		xtal1 = go.Scatter3d(name="Crystal +")
		xtal1.mode='lines'
		xtal_size = 0.2*zmax
		xtal1.x = xtal_size*np.array([1, 1,-1,-1,1,1, 1,-1,-1,1])
		xtal1.y = xtal_size*np.array([1,-1,-1, 1,1,1,-1,-1, 1,1])
		xtal1.z = d_cryst*np.array([1, 1, 1, 1, 1, 0, 0, 0, 0,0])
		
		pol1 = go.Scatter3d(name="P+",marker=dict(color='grey'))
		pol1.mode='lines'
		xtal_size = 0.2*zmax
		head = 0.1
		pol1.x = 0.7*xtal_size*np.array([0, 1, 1     , 1-head,1])
		pol1.y = 0.7*xtal_size*np.array([0, 1, 1-head, 1     ,1])
		pol1.z = d_cryst*np.array([0.5]*5) 

		annotations=[]
		if check_items[0] in chk:
			fig.add_trace(xtal1)
			fig.add_trace(pol1)
			annotations.extend([
				dict(
					text='L',
					x=idler_scatter.x[-1],
					y=idler_scatter.y[-1],
					z=idler_scatter.z[-1],
					arrowcolor='green',
				),
				dict(
					text='R',
					x=sig_scatter.x[-1],
					y=sig_scatter.y[-1],
					z=sig_scatter.z[-1],
					arrowcolor='green',
				),
				dict(
					text='z={0:.0f} um'.format(z[-1]),
					x=pump_scatter.x[-1],
					y=pump_scatter.y[-1],
					z=pump_scatter.z[-1],
					arrowcolor='green',
				),
				dict(
					text='P+',
					x=pol1.x[-1],
					y=pol1.y[-1],
					z=pol1.z[-1],
					arrowcolor='green',
				),
			])
		if check_items[1] in chk:
			fig.add_trace(axes)
			annotations.extend([
				dict(
					text='x (V)',
					x=axis_len,
					y=0,
					z=0,
					arrowcolor='blue',
				),
				dict(
					text='y (H)',
					x=0,
					y=axis_len,
					z=0,
					arrowcolor='blue',
				),
				dict(
					text='z',
					x=0,
					y=0,
					z=axis_len,
					arrowcolor='blue',
				),
			])
		fig.update_traces(hovertemplate=None,hoverinfo='skip')
		fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
#		fig.update_layout(autosize=False, width=800, height=400)
		
		fig.update_layout(
			scene=dict(
				aspectmode='manual',
				aspectratio=dict(x=zm*1,y=zm*1,z=zm*2),
				annotations=annotations,
				camera=dict(
					eye=dict(x=1,y=np.cos(yr),z=np.sin(yr)),
					projection=dict(type="orthographic"),
#					projection=dict(type="perspective"),
					up=dict(x=1,y=0,z=0),
				),
				xaxis=dict(
					showbackground=False,
					showline=False,
					showticklabels=False,
					title=dict(text=''),
					showspikes=False,
					range=[-zmax,zmax],
				),
				yaxis=dict(
					showbackground=False,
					showline=False,
					showticklabels=False,
					title=dict(text=''),
					showspikes=False,
					range=[-zmax,zmax],
				),
				zaxis=dict(
					showbackground=False,
					showline=False,
					showticklabels=False,
					title=dict(text=''),
					showspikes=False,
					range=[-zmax,zmax],
				),

				)
		)
	
		return fig 

except Exception as ex:
	logging.getLogger(__name__).error(__name__+" : Last chance exception:"+str(ex))
	logging.getLogger(__name__).info(__name__+" : Exit on last-chance exception")
finally:
	logging.getLogger(__name__).info(__name__+" : Reached finally OK")
