#!/usr/bin/node
let [, , a] = process.argv;
if (isNaN(a)) console.log('Missing number of occurrences');
else {
  for (a = parseInt(a); a > 0; a--) {
    console.log('C is fun');
  }
}
