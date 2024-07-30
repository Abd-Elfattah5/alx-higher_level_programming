#!/usr/bin/node

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const request = require('request');

request(url + id, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const info = JSON.parse(body);
    console.log(info.title);
  } else {
    console.log(err);
  }
}
);
