from flask import Flask
from flask import redirect
from flask import request
from flask import jsonify

from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)

load_dotenv(verbose=True)

REST_API_KEY = os.getenv('KEY')

REDIRECT_URI = 'http://localhost:3000/callback'


@app.route('/')
def redirected():
    return redirect(location=f'https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code&scope=profile account_email')


@app.route('/callback')
def callback():
    code = request.args.get('code')
    r = requests.post(f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&code={code}', headers={'Content-Type': 'application/json;charset=UTF-8'})
    access_token = r.json()['access_token']
    reque = requests.post('https://kapi.kakao.com/v2/user/me', headers={'Authorization' : f'Bearer {access_token}'})
    return jsonify(reque.json())


app.run(debug=True, host='127.0.0.1', port=3000)
