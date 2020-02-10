#!/usr/bin/node
exports.esrever = function (list) {
  const list1 = list;
  const list2 = [];
  for (let i = list1.length - 1; i >= 0; i--) {
    list2.push(list1[i]);
  }
  return list2;
};
