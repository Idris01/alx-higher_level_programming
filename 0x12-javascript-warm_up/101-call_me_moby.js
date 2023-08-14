#!/usr/bin/node

module.exports.callMeMoby = function (x, theFunction) {
  for (; x > 0; x--) theFunction();
};
