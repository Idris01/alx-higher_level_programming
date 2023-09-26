#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body);
    const tasks = {};
    for (const d of data) {
      const key = `${d.userId}`;
      const completed = d.completed;
      if (completed) {
        tasks[key] = tasks[key] ? tasks[key] + 1 : 1;
      }
    }
    console.log(tasks);
  }
});
