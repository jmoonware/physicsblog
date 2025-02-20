
import glob
import os
import logging
import importlib
import settings, os
import numpy as np
from datetime import datetime as dt

# the table of contents entries
toc_entries = []

class TocEntry:
	def __init__(self,date,title,description,logical_order,difficulty,topics,prerequisites=[]):
		self.date=dt.fromisoformat(date)
		self.date_iso=date
		self.title=title
		self.description=description
		self.logical=logical_order
		self.difficulty=difficulty # FIXME
		self.level=difficulty
		self.topics=topics
		self.location=None # filled in a run-time
		self.prerequisites=prerequisites

def update(post_path):
	raw_toc_entries=[]
	raw_files = glob.glob(os.path.join(settings.project_path,post_path,"*_meta.py"))
	for f in raw_files:
		fn = os.path.split(f)[-1].split('.')[0]
		candidate = importlib.import_module(post_path+"."+fn)
		logging.getLogger(__name__).info(str((post_path+"."+fn,candidate)))
		if hasattr(candidate, "toc"):
			logging.getLogger(__name__).info(str((fn, candidate.toc)))
			raw_toc_entries.append(candidate.toc)
			raw_toc_entries[-1].location=post_path+'.'+fn.split('_meta')[0]
		else:	
			logging.getLogger(__name__).info(str((fn,"No toc")))
	# default to date descending order
	dates = [te.date for te in raw_toc_entries]
	date_idx = np.argsort(dates)[::-1]
	toc_entries.extend([raw_toc_entries[i] for i in date_idx])

def get_topics():
	all_topics = []
	for te in toc_entries:
		for topic in te.topics:
			if not topic in all_topics:
				all_topics.append(topic)
	return all_topics

def get_sortitems():
	all_items = [
		'Date',
		'Logical',
		'Level',
	]
	return all_items

def get_recs(topics=[],sortby=[],sort_ascending=False):
	filtered_toc = []
	if topics!=None and len(topics) > 0:
		for te in toc_entries:
			for topic in topics:
				if topic in te.topics:
					filtered_toc.append(te)	
	else:
		[filtered_toc.append(te) for te in toc_entries]

	sort_vals = []
	if sortby!=None and len(sortby) > 0:
		for fe in filtered_toc:
			if hasattr(fe, sortby[0].lower()):
				sort_vals.append(getattr(fe,sortby[0].lower()))
	if len(sort_vals)==len(filtered_toc):
		if sort_ascending:
			sort_idx = np.argsort(sort_vals)
		else:
			sort_idx = np.argsort(sort_vals)[::-1]
		retvals = [filtered_toc[i] for i in sort_idx]
	else:
		retvals = filtered_toc
	return retvals
