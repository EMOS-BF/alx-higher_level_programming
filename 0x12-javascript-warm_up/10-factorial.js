#!/usr/bin/node
function factoriel (n) {
  if (!n) {
    return 1;
  } else {
    return n * factoriel(n - 1);
  }
}

const n = parseInt(process.argv[2]);
console.log(factoriel(n));
