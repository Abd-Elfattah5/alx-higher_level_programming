#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const info = JSON.parse(body);
    const movies = info.results;
    let num = 0;
    movies.forEach((movie) => {
      const actors = movie.characters;
      actors.forEach((actor) => {
        const id = actor.split('/')[5];
        if (id === '18') {
          num += 1;
        }
      });
    });
    console.log(num);
  } else {
    console.log(err);
  }
}
);
