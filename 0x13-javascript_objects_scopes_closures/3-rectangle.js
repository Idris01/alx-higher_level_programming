#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ([w, h].every((num) => num > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      const step = Buffer.alloc(this.width, 'X').toString();
      for (let i = 0; i < this.height; i++) {
        console.log(step);
      }
    }
  }
}
module.exports = Rectangle;
