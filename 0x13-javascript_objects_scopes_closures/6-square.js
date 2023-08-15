#!/usr/bin/node
const InitialSquare = require('./5-square.js');

class Square extends InitialSquare {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      const line = Buffer.alloc(this.width, c).toString();
      for (let i = 0; i < this.width; i++) {
        console.log(line);
      }
    }
  }
}

module.exports = Square;
