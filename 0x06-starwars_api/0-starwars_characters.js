#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');
// get movie id
if (process.argv.length !== 3) {
  console.error('Wrong usage: 0-starwars_characters.js [movie_id]');
  process.exit(-1);
}
const movieId = Number(process.argv[2]);
if (!movieId) {
  console.error('wrong format');
  process.exit(-1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
// Making the GET request
request(url, (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }

  // Checking the status code
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = data.characters;
    // for each character print its name
    for (const character of characters) {
      request(character, (err, response, body) => {
        if (error) {
          console.error(err);
        }
        if (response.statusCode === 200) {
          const data = JSON.parse(body);
          console.log(data.name);
        } else {
          console.log(`Request failed with status code: ${response.statusCode}`);
        }
      });
    }
  } else {
    console.log(`Request failed with status code: ${response.statusCode}`);
  }
});
