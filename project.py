import dash
import dash_bootstrap_components as dbc
from dash import html, Input, Output, State, ctx, dcc
from flask import request, Response, make_response
import flask
from dash.exceptions import PreventUpdate
import logging
from logging import handlers # why?
import settings

# utility functions
def StartDataLogging():
	logFormatString='\t'.join(['%(asctime)s','%(levelname)s','%(message)s'])
	level=logging.DEBUG
	maxbytes=1000000
	rfh=handlers.RotatingFileHandler(filename=settings.log_filename,maxBytes=maxbytes,backupCount=10)
	sh=logging.StreamHandler()
	logging.basicConfig(format=logFormatString,handlers=[sh,rfh],level=level)
	logging.captureWarnings(True)
	logger=logging.getLogger(__name__)
	logger.critical("Logging Started, level={0}".format(level))

########
# Start of exec
#######

StartDataLogging()

# start last-chance exception block
try:
	server=flask.Flask(__name__)
	app=dash.Dash(__name__,server=server,use_pages=True,
		external_stylesheets=[dbc.themes.BOOTSTRAP],
		eager_loading=True,
		meta_tags=[{'name':'viewport','content':'width=device-width, initial-scale=1'}]
			)
	app.title = 'John the Physicist'

	traprock_logo = 'assets/traprock_logo_crop.png'

	# Layout
	layout=[]
	layout.append(
		dbc.Row([
			dbc.NavbarSimple(
				children=[
					dbc.NavItem(dbc.NavLink("Contents",href=dash.page_registry['pages.toc']['path'])),
					dbc.NavItem(dbc.NavLink("About",href=dash.page_registry['pages.about']['path'])),
				],
				brand=dbc.Row(
					[
                        dbc.Col(dcc.Link(html.Img(src=traprock_logo, height="40px"),href=dash.page_registry['pages.home']['path'])),
                        dbc.Col(dbc.NavbarBrand("John the Physicist", className="ms-2",href=dash.page_registry['pages.home']['path'])),
                    ],
                    align="center",
				)
			),
		])
	)
	layout.append(
		dash.page_container
	)

	app.layout=html.Div(children=layout)

	# Endpoints
	@server.route('/about', methods=['GET'])
	def about_message():
		try:
			pass
		except Exception as ex:
			logging.getLogger(__name__).error("about: " + str(ex))
		return(Response(status=200))

except Exception as ex:
	logging.getLogger(__name__).error(__name__+ ": Last chance exception:"+str(ex))
	logging.getLogger(__name__).info(__name__+ ": Exit on last-chance exception")
finally:
	logging.getLogger(__name__).info(__name__+ ": Reached finally OK")
