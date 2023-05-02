SOURCES = ('source1', 'source2', 'source3')

def get_questions(connection, quantity):
	questions = {}

	for source in SOURCES:
		with connection.cursor() as cursor:
			cursor.execute(f'SELECT id, question, answer FROM questions WHERE source = "{source}" AND views < 1 LIMIT {quantity}')

		query_results = cursor.fetchall()
		questions[source] = query_results

		id_values = ', '.join([str(query_result[0]) for query_result in query_results])
		
		if id_values == '':
			continue

		with connection.cursor() as cursor:
			cursor.execute(f'UPDATE questions SET views = views + 1 WHERE id IN ({id_values})')

		connection.commit()
	
	return questions
