from flask import Flask
from flask import redirect
from flask import request

from dotenv import load_dotenv
import requests
import os

load_dotenv(verbose=True)
CLIENT_ID = os.getenv('CLIENT_ID')

app = Flask(__name__)


@app.route('/')
def redirected():
    return redirect(f'https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri=http%3A%2F'
                    f'%2Flocalhost%3A3000%2Fcallback&response_type=code&scope=identify%20email')


@app.route('/callback')
def callback():
    code = request.args.get('code')


app.run(host='127.0.0.1', port=3000)