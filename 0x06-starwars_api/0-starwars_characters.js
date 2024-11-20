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

// create new Promise to wrap request
const fetchCharacter = function (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, response, body) => {
      if (err) {
        reject(err);
      } else if (response.statusCode === 200) {
        const data = JSON.parse(body);
        // console.log(data.name); // Print character name
        resolve(data.name);
      } else {
        reject(new Error(`Request failed with status code: ${response.statusCode}`));
      }
    });
  });
};

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
// Making the GET request
const getCharacters = async function () {
  request(url, async (error, response, body) => {
    if (error) {
      console.error('An error occurred:', error);
      return;
    }

    // Checking the status code
    if (response.statusCode === 200) {
      const data = JSON.parse(body);
      // console.log(data);
      const characters = data.characters;
      // for each character print its name
      for (const character of characters) {
        const characterName = await fetchCharacter(character);
        console.log(characterName);
      }
    } else {
      console.log(`Request failed with status code: ${response.statusCode}`);
    }
  });
};
getCharacters();
