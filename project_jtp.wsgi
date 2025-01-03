import sys
sys.path.insert(0,'/opt/physicsblog')
sys.path.append('/opt/jtp-env')
sys.stdout=sys.stderr
from project_jtp import server as application
