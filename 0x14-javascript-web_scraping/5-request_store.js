#!/usr/bin/node

const fileName = process.argv[3];
const url = process.argv[2];
const fs = require('fs');
const request = require('request');

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(fileName, body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
