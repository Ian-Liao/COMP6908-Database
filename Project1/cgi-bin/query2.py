#!/usr/local/bin/python3

import cgi
import os

from jinja2 import Environment, FileSystemLoader

# Create instance of FieldStorage
from db_utils import cursor

form = cgi.FieldStorage()

# Get data from fields
cost = form.getvalue('cost', "")

query = '''SELECT DISTINCT s.sname
FROM Catalog c, Parts p, Suppliers s
WHERE c.pid = p.pid 
AND c.sid = s.sid
AND c.cost >= '{0}'
'''.format(cost)

cursor.execute(query)

res = cursor.fetchall()

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, '../htdocs')
env = Environment(loader=FileSystemLoader(templates_dir))
template = env.get_template('result.html')
print(template.render(res=res))
