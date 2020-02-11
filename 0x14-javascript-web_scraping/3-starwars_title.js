#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = 'http://swapi.co/api/films/' + movieId;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    // console.log(JSON.parse(body));
    const movieInfo = JSON.parse(body);
    console.log(movieInfo.title);
  }
});
