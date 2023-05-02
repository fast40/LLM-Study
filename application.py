from flask import Flask, request, send_file
import os

application = Flask(__name__)


@application.route('/')
def index():
	if 'quantity' in request.args:
		return os.environ.get('RDS_HOSTNAME')
	else:
		return 'LLM-Survey V1.0'
		

@application.route('/robots.txt')
def robots():
	return send_file('static/robots.txt')


if __name__ == '__main__':
	application.run(host='0.0.0.0', port=3000, debug=True)
