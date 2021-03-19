require('dotenv').config();
const app = require('express')();
const fetch = require('node-fetch');
const REDIRECT_URI = 'http://localhost:3000/callback';
const CLIENT_ID = process.env.CLIENT_ID;
const CLIENT_SECRET = process.env.CLIENT_SECRET

app.get('/', (req, res) => {
    res.redirect(`https://discord.com/api/oauth2/authorize?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=code&scope=identify%20email`)
})

app.get('/callback', async (req, res) => {
    const code = req.query.code;
    const params = new URLSearchParams({
        client_id: process.env.CLIENT_ID,
        code,
        client_secret: process.env.CLIENT_SECRET,
        redirect_uri: REDIRECT_URI,
        grant_type: 'authorization_code',
        scope: 'identify email guilds'
    })
    const token = (await (await fetch(`https://discord.com/api/v8/oauth2/token`, {
        method: 'POST',
        body: params,
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    })).json()).access_token;
    const userinfo = (await (await fetch(`https://discord.com/api/v8/users/@me`, {
        method: 'GET',
        headers: {
            Authorization: `Bearer ${token}`
        }
    })).json())
    res.send(userinfo);
})

app.listen(3000, () => {
    console.log('http://localhost:3000/ 에서 서버가 열리는중입니다!')
})