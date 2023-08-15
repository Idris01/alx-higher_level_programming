#!/usr/bin/node
const InitialSquare = require('./5-square.js');

class Square extends InitialSquare {
  charPrint (c) {
    let myChar = c;
    if (!myChar) {
      myChar = 'X';
    }
    if (this.width) {
      const line = Buffer.alloc(this.width, myChar).toString();
      for (let i = 0; i < this.width; i++) {
        console.log(line);
      }
    }
  }
}

module.exports = Square;
