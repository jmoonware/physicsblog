
import glob
import os
import logging
import importlib

# the table of contents entries
toc_entries = []

class TocEntry:
	def __init__(self,date,title,description,logical_order,difficulty,topics):
		self.date=date
		self.title=title
		self.description=description
		self.logical_order=logical_order
		self.difficulty=difficulty
		self.topics=topics

def update(post_path):
	raw_files = glob.glob(os.path.join(post_path,"*.py"))
	for f in raw_files:
		fn = os.path.split(f)[-1].split('.')[0]
		candidate = importlib.import_module(post_path+"."+fn)
		logging.getLogger(__name__).info(str((post_path+"."+fn,candidate)))
		if hasattr(candidate, "toc"):
			logging.getLogger(__name__).info(str((fn, candidate.toc)))
		else:	
			logging.getLogger(__name__).info(str((fn,"No toc")))
