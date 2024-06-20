#!/usr/bin/node

const list = require('./100-data').list;
const newList = list.map(e => e ** 2);
console.log(list);
console.log(newList);
