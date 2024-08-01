#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request({ url, method: 'GET' }, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const movies = JSON.parse(body);
    const wedge = 'https://swapi-api.alx-tools.com/api/people/18/';
    let count = 0;
    for (let a = 0; a < movies.count; a++) {
      const movieInArray = movies.results[a];
      if (movieInArray.characters.includes(wedge)) {
        count++;
      }
    }
    console.log(count);
  }
});
