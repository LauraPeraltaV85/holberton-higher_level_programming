#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const newDict = {};
    const tasksList = JSON.parse(body);
    // console.log(tasksList);
    for (let i = 0; i < tasksList.length; i++) {
      const newKey = tasksList[i].userId;
      // console.log(newKey);
      if (tasksList[i].completed === true && newDict[newKey]) {
        newDict[newKey] = newDict[newKey] + 1;
      } else if (tasksList[i].completed !== false && newDict[newKey] === undefined) {
        newDict[newKey] = 1;
      }
    }
    console.log(newDict);
  }
});
