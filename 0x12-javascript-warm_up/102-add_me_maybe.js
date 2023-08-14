#!/usr/bin/node

module.exports.addMeMaybe = function (x, theFunction) {
  const nb = ++x;
  theFunction(nb);
};
