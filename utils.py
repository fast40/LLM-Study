COLUMNS = ('id', 'qcat', 'qid', 'model', 'ResponseId', 'question', 'response', 'oversample', 'views')

def get_row(connection, model):
	connection.ping()
	
	with connection.cursor() as cursor:
		cursor.execute(f'SELECT * FROM data WHERE model = \'{model}\' AND views < 1 ORDER BY RAND() LIMIT 1')

	row = cursor.fetchone()

	try:
		with connection.cursor() as cursor:
			cursor.execute(f'UPDATE data SET views = views + 1 WHERE id = {row[0]}')
		
		connection.commit()
	except IndexError:
		pass

	return dict(zip(COLUMNS, row))
