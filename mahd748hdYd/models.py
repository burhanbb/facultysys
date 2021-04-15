import MySQLdb

db=MySQLdb.connect('localhost','root','root','newfaculty')

cursor=db.cursor()

print('connection done....')

