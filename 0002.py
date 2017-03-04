#!/usr/bin/env python
# coding=utf-8

import random, string, MySQLdb as mysqldb

def store_reldb():
	db = mysqldb.connect(host='localhost',user='root',passwd='123456',\
						 db = 'show_me_the_code')
	cursor = db.cursor()
	cursor.execute('drop table if EXISTS verify_info')
	sql = '''
		create table verify_info(
			id INT NOT NULL auto_increment PRIMARY KEY,
			verify_code CHAR(20)
		)'''
	cursor.execute(sql)

	verify_code = gen_charint(width = 20, num = 200)

	for code in verify_code:
		sql = 'INSERT INTO verify_info(verify_code) VALUES ("%s")' % code
		cursor.execute(sql)
		try:
			db.commit()
		except:
			db.rollback()
			print('Error happened when inserting data.')
	db.close()

def gen_charint(width, num):
	result = []
	charint = string.digits + string.letters
	for i in range(num):
		verify = [random.choice(charint) for j in range(width)]
		verify = ''.join(verify)
		result.append(verify)
	return result
if __name__ == '__main__':
	store_reldb()