#!/usr/bin/node

const fileName = process.argv[2];
const data = process.argv[3];
const fs = require('fs');

fs.writeFile(fileName, data, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
}
);
