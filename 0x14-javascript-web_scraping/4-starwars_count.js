#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (err, res, body) => {
  if (!err) {
    console.log(JSON.parse(body).films.length);
  }
});
