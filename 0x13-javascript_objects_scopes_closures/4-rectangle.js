#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let r;
    for (r = 0; r < this.height; r++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    this.height = [this.width, this.width = this.height][0];
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
