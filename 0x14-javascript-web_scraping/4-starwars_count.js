#!/usr/bin/node
const request = require('request');
const charUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
const url = process.argv[2];

request(url, (err, res, body) => {
  if (!err) {
    const data = JSON.parse(body).results;
    console.log(data.filter(item => item.characters.includes(charUrl)).length);
  }
});
