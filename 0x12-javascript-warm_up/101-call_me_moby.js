#!/usr/bin/node
module.exports = {
  callMeMoby: function (x, func) {
    let i;
    for (i = 0; i < x; i++) {
      func();
    }
  }
};
