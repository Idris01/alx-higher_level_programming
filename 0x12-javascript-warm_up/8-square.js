#!/usr/bin/node
let [, , a] = process.argv;
if (isNaN(a)) console.log('Missing size');
else {
  a = parseInt(a);
  const myStr = a > 0 ? Buffer.alloc(a, 'X').toString() : '';
  for (; a > 0; a--) {
    console.log(`${myStr}`);
  }
}
