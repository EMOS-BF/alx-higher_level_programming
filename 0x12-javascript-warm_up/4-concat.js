#!/usr/bin/node
if (!process.argv[2]) {
  process.argv[2] = 'undefined';
  process.argv[3] = 'undefined';
} else if (!process.argv[3]) {
  process.argv[3] = 'undefined';
}
console.log(process.argv[2] + ' ' + 'is' + ' ' + process.argv[3]);
