from flask import Flask, Response, request, send_file, jsonify
from utils import get_row
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
	if 'model' in request.args:
		row = get_row(connection, request.args['model'])
		
		response = jsonify(row)
		response.headers['Access-Control-Allow-Origin'] = '*'

		return response
	else:
		return 'LLM-Survey V1.0'
		

@application.route('/robots.txt')
def robots():
	return send_file('static/robots.txt')


if __name__ == '__main__':
	application.run(host='0.0.0.0', port=3000, debug=True)
