#!/usr/bin/node

exports.nbOccurences = function (a, b) {
  let i = 0;
  let c = 0;
  while (!(a[i] === undefined)) {
    if (a[i] === b) c++;
    i++;
  }
  return c;
};
