#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, res, body) {
  fs.writeFile(process.argv[3], body, 'UTF-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
