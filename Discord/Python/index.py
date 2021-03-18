from flask import Flask
from flask import redirect
from flask import request
from flask import jsonify

from dotenv import load_dotenv
import requests
import os

load_dotenv(verbose=True)
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:3000/callback'

app = Flask(__name__)


@app.route('/')
def redirected():
    return redirect(f'https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri=http%3A%2F'
                    f'%2Flocalhost%3A3000%2Fcallback&response_type=code&scope=identify%20email')


@app.route('/callback')
def callback():
    code = request.args.get('code')
    r = requests.post('https://discord.com/api/v8/oauth2/token', data={
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'scope': 'identify email'
    }, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    access_token = r.json()['access_token']
    requested = requests.get('https://discord.com/api/v8/users/@me', headers={
        'Authorization': f'Bearer {access_token}'
    })
    return jsonify(requested.json())


app.run(host='127.0.0.1', port=3000)
