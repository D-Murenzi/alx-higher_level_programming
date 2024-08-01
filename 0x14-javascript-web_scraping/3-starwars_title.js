#!/usr/bin/node

const request = require('request');
const urlStr = 'https://swapi-api.alx-tools.com/api/films/';
const urlGiven = urlStr + process.argv[2];
request({ url: urlGiven, method: 'GET' }, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
