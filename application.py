from flask import Flask
from flask import render_template

import requests

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    return render_template(
        'index.html', 
        access_token=get_access_token(),
        base_url='https://nitishsinghaltest-dev-ed.lightning.force.com/cometd/40.0/',
        channel_url='/event/DeveloperNitish__Notification__e'
    )


def get_access_token():
    """ Retrieve the access token by logging into Salesforce"""
    USERNAME = 'nitish.singhal89%40gmail.com'
    PASSWORD = 'nitish$0413'
    CONSUMER_KEY = '3MVG9Y6d_Btp4xp5unny4aRbPDHEYx_dE_GJtWEHYBWvWQC.ehqqnJR9f.eI6SxEeDNg_x6z0t5HsW6FGR.5Q'
    CONSUMER_SECRET = '6377572954480626031'
    url = 'https://login.salesforce.com/services/oauth2/token'
    body = 'grant_type=password&client_id=%s&client_secret=%s&username=%s&password=%s' % (CONSUMER_KEY, CONSUMER_SECRET, USERNAME, PASSWORD)
    result = requests.post(url, data=body, headers={'Content-Type':'application/x-www-form-urlencoded'})
    return result.json().get('access_token')