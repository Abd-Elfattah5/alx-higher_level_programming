#!/usr/bin/node
exports.esrever = function (list) {
  const revlist = [];
  for (let i = list.length ; i > 0; i--) {
    revlist.push(list[i - 1]);
  }
  return list;
};
