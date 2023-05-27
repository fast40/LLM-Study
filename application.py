from flask import Flask, request, send_file, jsonify
from utils import get_row

application = Flask(__name__)


@application.route('/')
def index():
	if 'model' in request.args:
		row = get_row(request.args['model'])
		
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
