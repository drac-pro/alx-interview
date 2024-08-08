#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, { json: true }, (err, res, body) => {
  if (!err) {
    body.characters.forEach(character => {
      request(character, { json: true }, (err2, res2, body2) => {
        if (!err2) { console.log(body2.name); }
      });
    });
  }
});
