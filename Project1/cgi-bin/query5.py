#!/usr/local/bin/python3

import cgi
import os

from jinja2 import Environment, FileSystemLoader

# Create instance of FieldStorage
from db_utils import cursor

form = cgi.FieldStorage()

# Get data from fields
address = form.getvalue('address', "")

query = '''SELECT s.sid, s.sname
FROM Suppliers s
WHERE s.address = '{0}'
AND s.sid NOT IN 
(SELECT DISTINCT c.sid FROM Catalog c)
'''.format(address)

cursor.execute(query)

res = cursor.fetchall()

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, '../htdocs')
env = Environment(loader=FileSystemLoader(templates_dir))
template = env.get_template('result.html')
print(template.render(res=res))
