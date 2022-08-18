var favoriteMovie = function displayFavorite(movieName) {
  console.log("My favorite movie is " + movieName);
};
function movies(messageFunction, name) {
  messageFunction(name);
}
movies(favoriteMovie, "Finding Nemo");

// or

function movies(messageFunction, name) {
  messageFunction(name);
}
movies(function displayFavorite(movieName) {
  console.log("My favorite movie is " + movieName);
}, "Finding Nemo");