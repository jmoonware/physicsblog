
import glob
import os
import logging
import importlib
import pandas as pd 
import settings, os

# the table of contents entries
toc_entries = []

class TocEntry:
	def __init__(self,date,title,description,logical_order,difficulty,topics,prerequisites=[]):
		self.date=date
		self.title=title
		self.description=description
		self.logical_order=logical_order
		self.difficulty=difficulty
		self.topics=topics
		self.location=None # filled in a run-time
		self.prerequisites=prerequisites

def update(post_path):
	raw_files = glob.glob(os.path.join(settings.project_path,post_path,"*_meta.py"))
	for f in raw_files:
		fn = os.path.split(f)[-1].split('.')[0]
		candidate = importlib.import_module(post_path+"."+fn)
		logging.getLogger(__name__).info(str((post_path+"."+fn,candidate)))
		if hasattr(candidate, "toc"):
			logging.getLogger(__name__).info(str((fn, candidate.toc)))
			toc_entries.append(candidate.toc)
			toc_entries[-1].location=post_path+'.'+fn.split('_meta')[0]
		else:	
			logging.getLogger(__name__).info(str((fn,"No toc")))

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

def get_recs(topics=[]):
	filtered_toc = []
	if topics!=None and len(topics) > 0:
		for te in toc_entries:
			for topic in topics:
				if topic in te.topics:
					filtered_toc.append(te)	
	else:
		[filtered_toc.append(te) for te in toc_entries]

	return filtered_toc
