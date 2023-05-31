import pymysql
import os

RDS_HOSTNAME = os.environ.get('RDS_HOSTNAME')
RDS_PORT = int(os.environ.get('RDS_PORT'))
RDS_DB_NAME = os.environ.get('RDS_DB_NAME')
RDS_USERNAME = os.environ.get('RDS_USERNAME')
RDS_PASSWORD = os.environ.get('RDS_PASSWORD')

COLUMNS = ('id', 'qcat', 'qid', 'model', 'ResponseId', 'question', 'response', 'oversample', 'views')

def get_row(model):
	with pymysql.connect(host=RDS_HOSTNAME, user=RDS_USERNAME, passwd=RDS_PASSWORD, port=RDS_PORT, database=RDS_DB_NAME, ssl_ca='us-west-1-bundle.pem', autocommit=True) as connection, connection.cursor() as cursor:
		cursor.execute(f'SELECT * FROM data WHERE model = \'{model}\' AND views < 1 ORDER BY RAND() LIMIT 1')
		row = cursor.fetchone()

		if row:
			cursor.execute(f'UPDATE data SET views = views + 1 WHERE id = {row[0]}')
		else:
			row = [0, 0, 0, '', '', 'No more questions available.', 'Please continue without answering survey questions.', 0, 0]

		return dict(zip(COLUMNS, row))  # returns empty dict if row is empty list
