#!/usr/bin/node
const [, , a, b] = process.argv;

add(a, b);

function add (a, b) {
  console.log(`${parseInt(a) + parseInt(b)}`);
}
