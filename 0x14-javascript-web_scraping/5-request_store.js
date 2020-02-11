#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const text = JSON.parse(body);
    fs.writeFile(filePath, text, 'utf8', err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
