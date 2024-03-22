#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  charPrint (c = 'X') {
    for (let b = 0; b < this.height; b++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
