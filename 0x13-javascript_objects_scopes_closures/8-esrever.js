#!/usr/bin/node
exports.esrever = function (list) {
  // function that returns the reversed version of a list
  const reverselist = [];
  for (let i = list.length - 1; i > 0; i--) {
    reverselist.push(list[i]);
  }
  return reverselist;
};
