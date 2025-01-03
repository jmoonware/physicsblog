import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import logging
import glob
import settings,os

dash.register_page(__name__,title="John the Physicist")

# logging.getLogger(__name__).error('files are ' + str(glob.glob('*')))

with open(os.path.join(settings.project_path,'bellcalcs.py')) as f:
	code_text = ''.join(f.readlines())

layout = html.Div([
	dbc.Row([
		dcc.Markdown(" 1. Recall that Venn diagrams are _schematic_. Although everything within the square boundary represents a total probability of '1', the normalized sub-area(s) in the diagram aren't necessarily exactly equal to their corresponding probabilities. The areas may not even be _relatively_ proportional to probability in some cases (i.e. a smaller area might not actually have a smaller probability than a larger area, etc."),
		dcc.Markdown(" 2. Technically, this is only one of a set of equations that can be called Bell's Inequality. There are other equally valid ways to choose settings that lead to non-trivial inequalities."),
		dcc.Markdown(" 3. Here is the full code used to generate the Bell statistics. The output of the function *gen_bell_stats* is what is plotted as points:\n```"+code_text+"\n```"),
		],  
		justify='center'),
])
