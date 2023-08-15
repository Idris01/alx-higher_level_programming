#!/usr/bin/node
exports.converter = function (base) {
  return function (value) {
    return parseInt(value, 10).toString(base);
  };
};
