#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) & (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const x = 'X';
    for (let a = 0; a < this.height; a++) {
      console.log(x.repeat(this.width));
    }
  }

  rotate () {
    const x = this.width;
    const y = this.height;
    this.width = y;
    this.height = x;
  }

  double () {
    const x = this.width;
    const y = this.height;
    this.width = x * 2;
    this.height = y * 2;
  }
}
module.exports = Rectangle;
