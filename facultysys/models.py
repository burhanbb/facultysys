import MySQLdb

db=MySQLdb.connect('localhost','root','root','facultysys')

cursor=db.cursor()

print('connection done....')

