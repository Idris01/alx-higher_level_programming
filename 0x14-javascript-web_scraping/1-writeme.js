#!/usr/bin/node
const fs = require('node:fs/promises');
const path = process.argv[2];
const content = process.argv[3];

(async () => {
  try {
    const file = await fs.open(path, 'w');
    await file.write(content);
  } catch (error) {
    console.log(error);
  }
})();
