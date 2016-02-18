import pymysql.cursors
import html2text

db = pymysql.connect(host='localhost',
	user='root', password='', db='joomla',
	charset='utf8')

def write_md(page):
	name = 'crunch_' + page[1] + '.md'
	front_matter = '---\ntitle: "{}"\naudience: all\n---\n\n'.format(page[0])
	with open(name, 'w') as file:
		file.write(front_matter)
		file.write(html2text.html2text(page[2]).encode('utf8'))
		file.write('\n')


with db.cursor() as cursor:
	cursor.execute('select `title`, `alias`, `introtext` from content;')
	for page in cursor.fetchall():
		write_md(page)
