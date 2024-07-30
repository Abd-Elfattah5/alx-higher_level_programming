#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const emp = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0 };

request(url, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const info = JSON.parse(body);
    for (const task of info) {
      if (task.completed === true) {
        emp[Number(task.userId)] += 1;
      }
    }
    console.log(emp);
  } else {
    console.log(err);
  }
});
