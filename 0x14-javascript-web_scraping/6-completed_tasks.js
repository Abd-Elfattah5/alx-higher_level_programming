#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const info = JSON.parse(body);
    const emp = {};
    for (const task of info) {
      if (task.completed && !emp[task.userId]) {
        emp[task.userId] = 0;
      }
      if (task.completed === true) {
        emp[Number(task.userId)] += 1;
      }
    }
    console.log(emp);
  } else {
    console.log(err);
  }
});
