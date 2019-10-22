#!/usr/local/bin/python3

import os
import cgi
from jinja2 import Environment, FileSystemLoader

from db_utils import cursor

# Create instance of FieldStorage
form = cgi.FieldStorage() 

# Get data from fields
part_name = form.getvalue('part_name', "")
sid = form.getvalue('sid', "")
sname = form.getvalue('sname', "")
address = form.getvalue('address', "")
cost = form.getvalue('cost', "")

fields = [sid, sname, address, cost]
query = '''SELECT {1}
FROM Catalog c, Parts p, Suppliers s
WHERE c.pid = p.pid 
AND c.sid = s.sid
AND p.pname = '{0}'
'''.format(part_name, ", ".join((f for f in fields if f)))

cursor.execute(query)

res = cursor.fetchall()

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, '../htdocs')
env = Environment(loader=FileSystemLoader(templates_dir))
template = env.get_template('result.html')
print(template.render(res=res))
