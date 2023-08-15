#!/usr/bin/node
exports.esrever = function (list) {
  function reverseList (list) {
    if (list.length <= 1) return list;
    const [val, ...data] = list;
    return [...reverseList(data), val];
  }
  return reverseList(list);
};
