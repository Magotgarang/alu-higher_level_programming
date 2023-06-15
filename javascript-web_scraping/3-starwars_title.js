#!/usr/bin/node

const request = require('request');

const id = process.argv[2];

request.get('https://swapi-api.alx-tool.com/api/flims/${id}`, function (err, res)
  if (err) {
    console.log(err);
} else {
    console.log(JSON.parse(res.body).title);
}
});
