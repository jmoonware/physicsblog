import sys
sys.path.insert(0,'/var/www/traprockllc')
sys.path.append('/var/www/www-env')
sys.stdout=sys.stderr
from project import server as application