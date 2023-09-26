#!/usr/bin/node
const fs = require('node:fs/promises');
const path = process.argv[2];

(async () => {
  try {
    const file = await fs.open(path, 'r');
    const data = await file.read(encoding="utf-8");
    console.log(data.buffer.toString());
  } catch (error) {
    console.log(error);
  }
})();
