#!/usr/bin/node
const [, , a] = process.argv;

console.log(factoria(a));

function factoria (num) {
  if (+num < 0) return 0;
  if (isNaN(num)) return 1;
  if (parseInt(num) === 1) return 1;

  num = parseInt(num);
  return num * factoria(num - 1);
}
