#!/usr/bin/node
exports.logMe = (function (item) {
  let argPrinted = 0;
  return function (item) {
    console.log(`${argPrinted}: ${item}`);
    argPrinted++;
  };
}());
