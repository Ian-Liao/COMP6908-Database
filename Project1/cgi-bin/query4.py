#!/usr/local/bin/python3

# import sys
import cgi
import os

from jinja2 import Environment, FileSystemLoader

# Create instance of FieldStorage
from db_utils import cursor

form = cgi.FieldStorage()

# Get data from fields
color = form.getvalue('color', "")
address = form.getvalue('address', "")

# sys.stderr = sys.stdout

query = '''SELECT P.pname
FROM Parts P
WHERE P.color = '{0}' AND NOT EXISTS
(SELECT S1.sid
		FROM Suppliers S1
		WHERE S1.address = '{1}' AND S1.sid NOT IN
		(SELECT C.sid
			FROM Catalog C, Suppliers S2
			WHERE C.sid = S2.sid AND S2.address = '{1}' AND C.pid = P.pid))
'''.format(color, address)

cursor.execute(query)

res = cursor.fetchall()

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, '../htdocs')
env = Environment(loader=FileSystemLoader(templates_dir))
template = env.get_template('result.html')
print(template.render(res=res))
