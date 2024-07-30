#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/people/18';
const request = require('request');

request(url, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const info = JSON.parse(body);
    const movies = info.films.length;
    console.log(movies);
  } else {
    console.log(err);
  }
}
);
