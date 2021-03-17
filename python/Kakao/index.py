from flask import Flask
from flask import redirect

from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv(verbose=True)

REST_API_KEY = os.getenv('KEY')

REDIRECT_URI = 'http://localhost:3000/callback'


@app.route('/')
def redirected():
    return redirect(location=f'https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code')


@app.route('/callback')
def callback():
    return 'ㅋㅋㄹ'


app.run(debug=True, host='127.0.0.1', port=3000)
