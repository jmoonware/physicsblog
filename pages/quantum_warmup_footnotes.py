import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import logging
import glob
import settings,os

dash.register_page(__name__,title="John the Physicist")

layout = html.Div([
	dbc.Row([
		dcc.Markdown(r"1. Like many things in quantum computing, devices that show up in theoretical descriptions are more aspirational than actual. In the case of the 'photon on demand' [gizmo](https://pubs.acs.org/doi/10.1021/acsphotonics.3c00973), this is still very much an active research area. There is at least one company that is working on them: [Quandela](https://www.quandela.com/technology/the-power-of-single-photon-sources/). Here is a recent [2025](https://spie.org/news/photonics-focus/janfeb-2025/hunting-for-the-perfect-single-photon-source) link to a discussion on the present state-of-the-art published by SPIE.",mathjax=True), 
		dcc.Markdown(r"2. For those of you who have played with [Discrete Fourier Transforms](https://en.wikipedia.org/wiki/Discrete_Fourier_transform), you can immediately see how this might be used (the alternating +/1 weights are just a simple example of using $e^{ikn}$ as weights.) This will become very important later.",mathjax=True), 
		dcc.Markdown(r"3. See for instance this [link](https://thequantuminsider.com/2023/12/29/quantum-computing-companies/). Eventually I will summarize these in a better table. There are roughly 40 start-up companies, plus extensive research at Google, Meta, Microsoft, etc. Damn, people really want to break RSA encryption...",mathjax=True), 
		dcc.Markdown(r"4. Incidentally, the situation appears to be like the very early days of semiconductors, where it wasn't clear what the best material would be to build large arrays of transistors (germanium? gallium arsenide? silicon? ...) Also, in the very early days of microchips, it was almost impossible to make a chip that worked, since the defect rate was so high. Error correction was tried, and eventually abandoned in favor of clean rooms and _just make every chip perfect_. That approach was far-fetched at one point, but today the big fabs have an extraordinarily low defect rate (TSMC achieves something like 0.1 defect per square cm.)",mathjax=True), 
		], 		
		justify='center'),
])
