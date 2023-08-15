#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ([w, h].every((num) => num > 0)) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
