#!/usr/bin/node
const arg1 = Number(process.argv[2]);
if (isNaN(arg1)) {
  console.log('Missing number of occurrences');
} else {
  let i = arg1;
  while (i > 0) {
    console.log('C is fun');
    i--;
  }
}
