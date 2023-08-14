#!/usr/bin/node
// get the supplied arguments
let [, , ...nums] = process.argv;

nums = nums.map(item => parseInt(item));

if (nums.length <= 1) console.log(0);

else {
  nums = nums.sort((a, b) => a >= b ? -1 : 1);
  console.log(nums[1]);
}
