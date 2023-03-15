#!/usr/bin/node
let i = 0;
const array = [];
for (i = 2; i < process.argv.length; i++) {
  array.push(parseInt(process.argv[i]));
}

let j = 0;
let biggest = array[0];
let index = 0;
for (j = 0; j < array.length; j++) {
  if (array[j] > biggest) {
    biggest = array[j];
    index = j;
  }
}
array.splice(index, 1);
let k = 0;
let secondBig = 0;
for (k = 0; k < array.length; k++) {
  if (array[k] > secondBig) {
    secondBig = array[k];
  }
}

console.log(secondBig);
