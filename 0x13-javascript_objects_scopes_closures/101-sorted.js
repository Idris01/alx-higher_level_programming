#!/usr/bin/node
const { dict } = require('./101-data');
const newDict = {};
const newKeys = [];
Object.values(dict).forEach(item => {
  if (!newKeys.includes(item)) newKeys.push(item);
});
newKeys.sort();
newKeys.forEach(item => {
  newDict[item] = [];
});
for (const itm in dict) {
  newDict[dict[itm]].push(itm);
}
console.log(newDict);
