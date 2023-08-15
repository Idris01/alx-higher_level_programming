#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((a, b) => a + (b === searchElement ? 1 : 0), 0);
};
