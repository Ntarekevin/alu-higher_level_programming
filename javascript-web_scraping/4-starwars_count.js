#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const wedgeId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  let count = 0;

  for (const film of data.results) {
    for (const characterUrl of film.characters) {
      if (characterUrl.includes(`/people/${wedgeId}/`)) {
        count++;
        break;
      }
    }
  }

  console.log(count);
});
