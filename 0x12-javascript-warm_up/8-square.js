#!/usr/bin/node
const arg1 = Number(process.argv[2]);
if (isNaN(arg1)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg1; i++) {
    let row = '';
    for (let j = 0; j < arg1; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
