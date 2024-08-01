#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const URL = process.argv[2];
const filepath = process.argv[3];
request({ url: URL, method: 'GET' }, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(filepath, body, 'utf8', function (err) {
      if (err) {
        console.error(err);
      }
    });
  }
});
