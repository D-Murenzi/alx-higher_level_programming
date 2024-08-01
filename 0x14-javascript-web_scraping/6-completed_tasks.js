#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];
request({ url: URL, method: 'GET' }, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const todos = JSON.parse(body);
    const obj = {};
    for (let a = 0; a < todos.length; a++) {
      if ((!(todos[a].userId in obj)) && todos[a].completed) {
        obj[todos[a].userId] = 1;
      } else if ((todos[a].userId in obj) && todos[a].completed) {
        obj[todos[a].userId]++;
      }
    }
    console.log(obj);
  }
});
