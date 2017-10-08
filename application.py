from flask import Flask
from flask import render_template

import requests

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    return render_template('index.html', access_token=get_access_token())


def get_access_token():
    """ Retrieve the access token by logging into Salesforce"""
    USERNAME = 'ben%40edwards.nz'
    PASSWORD = 'google12'
    CONSUMER_KEY = '3MVG99qusVZJwhsnmdmjq1uHdUrHw7YM6LakYhCxhvP3IMzoLXUB_cjFdpUhGMttiN7ooMHs3sTIF6emzDyzh'
    CONSUMER_SECRET = '2335697909761120514'
    url = 'https://login.salesforce.com/services/oauth2/token'
    body = 'grant_type=password&client_id=%s&client_secret=%s&username=%s&password=%s' % (CONSUMER_KEY, CONSUMER_SECRET, USERNAME, PASSWORD)
    result = requests.post(url, data=body, headers={'Content-Type':'application/x-www-form-urlencoded'})
    return result.json().get('access_token')