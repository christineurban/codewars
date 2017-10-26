// https://www.codewars.com/kata/duck-duck-goose

function duckDuckGoose(players, goose) {
 
  if (goose <= players.length) {
    return players[goose-1].name;
  }
  
  else if (goose % players.length == 0){
    return players[players.length-1].name;
  }
  else return players[goose % players.length-1].name;
}