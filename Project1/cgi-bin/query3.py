#!/usr/local/bin/python3

import cgi
import os

from jinja2 import Environment, FileSystemLoader

# Create instance of FieldStorage
from db_utils import cursor

form = cgi.FieldStorage()

# Get data from fields
pid = form.getvalue('pid', "")

query = '''SELECT s.sname, s.address
FROM Catalog c, Suppliers s
WHERE c.sid = s.sid
AND c.pid = '{0}'
AND c.cost = (
SELECT MAX(c1.cost) 
FROM Catalog c1 
WHERE c1.pid = '{0}')
'''.format(pid)

cursor.execute(query)

res = cursor.fetchall()

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, '../htdocs')
env = Environment(loader=FileSystemLoader(templates_dir))
template = env.get_template('result.html')
print(template.render(res=res))
