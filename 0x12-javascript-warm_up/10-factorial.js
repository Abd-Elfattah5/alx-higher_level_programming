#!/usr/bin/node
const arg = process.argv[2];

function factorial (a) {
  if (a <= 1) {
    return 1;
  }
  return factorial(a - 1) * a;
}

if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(factorial(arg));
}
