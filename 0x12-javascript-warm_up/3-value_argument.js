#!/usr/bin/node
const { argv } = require('node:process');
const args = Object.values(argv);
const len = Object.keys(argv).length - 2;
if (len < 1) {
  console.log('No Arguments');
} else {
  console.log(args[2]);
}
