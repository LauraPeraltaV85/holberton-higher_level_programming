#!/usr/bin/node
const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let r = 0; r < this.width; r++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
