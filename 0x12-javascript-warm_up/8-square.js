#!/usr/bin/node
let i = 0;
if (!parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  while (i < process.argv[2]) {
    console.log('X'.repeat(process.argv[2]));
    i++;
  }
}
