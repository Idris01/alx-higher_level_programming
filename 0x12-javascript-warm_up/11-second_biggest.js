#!/usr/bin/node
// get the supplied arguments
let [, , ...nums] = process.argv;

nums = nums.map(item => parseInt(item));

if (nums.length <= 1) console.log(0);

else if (nums.length === 2) console.log(Math.max(...nums));
else {
  nums = nums.sort((a, b) => a >= b ? -1 : 1);
  const newList = [];
  for (const item of nums) {
    if (newList.length === 2) {
      console.log(newList[1]);
      break;
    }
    !newList.includes(item) && newList.push(item);
  }
  // all numbers in the list are equal
  if (newList.length === 1) console.log(0);
}
