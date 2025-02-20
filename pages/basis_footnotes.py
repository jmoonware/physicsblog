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
		dcc.Markdown(r"1. Mathematicians are cringing here - this sum has a well-defined convergence criterion, so no, not all functions can be transformed with any old basis function. But most of the functions in physics we will encounter here are going to be fine.",mathjax=True), 
		dcc.Markdown(r"2. More accurately, the Dirac Delta has an area of one - it's infinitely thin and infinitely high, but the product of width times height is one.",mathjax=True), 
		dcc.Markdown(r"3. In order to make a set of orthonormal polynomials, we need to define a better inner product. To make the integral converge above, the inner product would need a _weighting function_. A weighting function keeps the integral from blowing up. And what always goes to zero faster than any power of $x$? Our old buddy $e^x$ of course. If we weight by $e^{-x}$ (and keep the $x$'s positive) we get [Laguerre](https://en.wikipedia.org/wiki/Laguerre_polynomials) polynomials. If we use $e^{-x^2}$ (where now $x$ can be any value) we get [Hermite](https://en.wikipedia.org/wiki/Hermite_polynomials) polynomials. These orthonormal polynomials show up when studying the hydrogen atom and quantum harmonic oscillator, respectively. We can also restrict the interval (rather than trying to integrate over infinity.) For instance, [Legendre](https://en.wikipedia.org/wiki/Legendre_polynomials) polynomials have an inner product defined over the range $x \in [-1,1]$. And, even more interesting, we can derive the Taylor expansion from the limit of a Legendre polynomial expansion, as is done [here](assets/taylor_series_fishback.pdf).",mathjax=True), 
		], 
		justify='center'),
])
