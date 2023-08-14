#!/usr/bin/node
let counter = 0;

process.argv.forEach(() => counter++);

if (counter === 2) console.log('No argument');
else console.log(`${process.argv[2]}`);
