from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api',methods=['GET'])
def get_info():
    #getting(retrieving) query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    #getting the current day of the week
    current_date = datetime.datetime.now().strftime('%A')

    #getting the utc time
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    github_file_url = 