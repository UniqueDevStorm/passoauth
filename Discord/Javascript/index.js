require('dotenv').config();
const app = require('express')();
const axios = require('axios');
const REDIRECT_URI = 'http://localhost:3000/callback';
const CLIENT_ID = process.env.CLIENT_ID;

app.get('/', (req, res) => {
    res.redirect(`https://discord.com/api/oauth2/authorize?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=code&scope=identify%20email`)
})

app.get('/callback', (req, res) => {
    const code = req.query.code;
    res.send(code);
})

app.listen(3000, () => {
    console.log('http://localhost:3000/ 에서 서버가 열리는중입니다!')
})