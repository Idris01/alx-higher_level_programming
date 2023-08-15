#!/usr/bin/node
const fs = require('fs');
const [, , fileA, fileB, fileC] = process.argv;

const stream1 = fs.readFileSync(fileA);
const stream2 = fs.readFileSync(fileB);
fs.writeFileSync(fileC, stream1 + stream2);
