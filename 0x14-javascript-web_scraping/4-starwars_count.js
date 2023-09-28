#!/usr/bin/node
const request = require('request');
const charUrl = 'people/18/';
const url = process.argv[2];

request(url, (err, res, body) => {
  if (!err) {
    const data = JSON.parse(body).results;
    const chaData = data.filter(({ characters }) => {
      for (const cha of characters) {
        if (cha.endsWith(charUrl)) return true;
      }
      return false;
    });
    console.log(chaData.length);
  }
});
