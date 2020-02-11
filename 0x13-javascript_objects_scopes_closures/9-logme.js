#!/usr/bin/node
let i = 1;
exports.logMe = function (item) {
  const j = -1;
  const k = i + j;
  console.log(k + ': ' + item);
  i++;
};
