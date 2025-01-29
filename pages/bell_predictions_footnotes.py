import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import logging
import glob
import settings,os

dash.register_page(__name__,title="John the Physicist")

# logging.getLogger(__name__).error('files are ' + str(glob.glob('*')))

#with open(os.path.join(settings.project_path,'bellcalcs.py')) as f:
#	code_text = ''.join(f.readlines())

layout = html.Div([
	dbc.Row([
		dcc.Markdown(r"1. An electron-Volt (eV) is the kinetic energy an electron gets when accelerated through a 1 V potential, i.e. $1.6\times10^{-19}$ Joules. It is $\Large{\varepsilon}\normalsize{= 1.24e/\lambda}$, where $\lambda$ is the wavelength in microns. That's about $2\times10^{-19}$ Joules for a 1 $\mu$m wavelength, or 0.2 attojoules. Semiconductor people like working in eV rather than attojoules. Go figure.",mathjax=True), 
		dcc.Markdown(r"2. Note the normalization factor $1/\sqrt{r^2+(1-r)^2}$. This is actually just 1 (since $r$ is _either_ 0 or 1). I included it explicitly because this factor becomes the familiar $1/\sqrt{2}$ when we set $r$ and $(1-r)$ to 1 in the quantum case.",mathjax=True), 
		dcc.Markdown(r"3. The quantum rotation matrix turns out to be the unitary rotation of a Pauli spin matrix. That will require its own post to explain.",mathjax=True), 		
		dcc.Markdown(r"4. Physicists have an elegant notation called 'bra-ket' that generalizes out the need to display the spatial $\mathbf{r}_L, \mathbf{r}_R$ variables. Rather than eigenfunctions $\psi$, states are 'kets' denoted solely with quantum numbers (in this case, $H$ and $V$.) An example of this would be $\left|HV\right>$. The conjugate 'bra' of this state is $\left<HV\right|$, and where the inner product $\left<HV|HV\right> = 1$. I didn't use the (admittedly simpler) bra-ket notation here in order to better see the correspondence between classical and quantum calculations.",mathjax=True),
		], 
		justify='center'),
])
