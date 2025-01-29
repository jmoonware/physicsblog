import re
import os
from dash import html, dcc
import settings, os

def get_section(file, start='', end=''):
	''' Args: 
			file:  Python module name e.g. 'subdir.module' format
		 	That allows using __name__ as the file
			Supplying the raw name without the .txt extension should work too
	'''
	section=[]
	# strip off trailing stuff
	fn = file.replace('.py','').replace('_meta','')
	# replace python . with os path sep and add file type postfix
	fn = fn.replace('.',os.sep)+'.txt'
	start_pattern = re.escape('[comment]: # ('+start+')')
	end_pattern = re.escape('[comment]: # ('+end+')')
	if len(start)>0:
		is_section=False
	else: # just start collecting
		is_section=True
	with open(os.path.join(settings.project_path,fn),'r') as f:
		for l in f.readlines():
			if re.search(start_pattern,l):
				is_section=True
			if is_section:
				if re.search(end_pattern,l):
					break
				else:
					section.append(l)
	
	return(''.join(section))

def build_markdown(name,start,end,image_path,body=[],width=300):
	body.append(
		dcc.Markdown(
			get_section(name,start=start,end=end),
			mathjax=True,
		)
	)
	if image_path!=None:
		body.append(
			html.Img(src=image_path, width=width)
		)
	return
