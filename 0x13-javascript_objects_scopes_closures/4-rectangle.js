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

  rotate () {
    if (this.width && this.height) {
      const temp = this.height;
      this.height = this.width;
      this.width = temp;
    }
  }

  double () {
    if (this.width && this.height) {
      this.height = this.height * 2;
      this.width = this.width * 2;
    }
  }
}
module.exports = Rectangle;
