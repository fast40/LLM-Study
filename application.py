from flask import Flask, request, send_file
from utils import get_questions
import pymysql
import boto3
import os

application = Flask(__name__)

RDS_HOSTNAME = os.environ.get('RDS_HOSTNAME')
RDS_PORT = int(os.environ.get('RDS_PORT'))
RDS_DB_NAME = os.environ.get('RDS_DB_NAME')
RDS_USERNAME = os.environ.get('RDS_USERNAME')
RDS_PASSWORD = os.environ.get('RDS_PASSWORD')

session = boto3.Session()
client = session.client(service_name='rds', region_name='us-west-1')
connection =  pymysql.connect(host=RDS_HOSTNAME, user=RDS_USERNAME, passwd=RDS_PASSWORD, port=RDS_PORT, database=RDS_DB_NAME, ssl_ca='us-west-1-bundle.pem')

@application.route('/')
def index():
	if 'quantity' in request.args:
		return get_questions(connection, request.args['quantity'])
	else:
		return {'LLM-Survey V1.0': [RDS_HOSTNAME, RDS_USERNAME, RDS_PASSWORD, RDS_PORT, RDS_DB_NAME]}
		

@application.route('/robots.txt')
def robots():
	return send_file('static/robots.txt')


if __name__ == '__main__':
	application.run(host='0.0.0.0', port=3000, debug=True)
