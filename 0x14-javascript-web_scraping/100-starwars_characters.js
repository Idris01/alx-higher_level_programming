#!/usr/bin/node
const util = require('util');
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
const requestPromise = util.promisify(request);

const nameDict = {};
requestPromise(url)
  .then(data => {
    const { characters } = JSON.parse(data.body);
    let count = characters.length;
    characters.forEach(cha => {
      const id = cha.match(/\d+/)[0];
      requestPromise(cha)
        .then(thisChar => {
          nameDict[id] = JSON.parse(thisChar.body).name;
        })
        .catch(thisErr => {
          console.log(thisErr);
        })
        .finally(() => {
          count--;
          if (count === 0) {
            Object.values(nameDict).forEach(val => console.log(val));
          }
        });
    });
  })
  .catch(err => {
    console.log(err);
  });
