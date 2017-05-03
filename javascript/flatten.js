// https://www.codewars.com/kata/flatten-1

var flatten = function (array){
  var finalArray = [];
  for (var inner of array) {
    if (typeof inner === "string" || typeof inner === "number") {
      finalArray.push(inner);
    } else {
      for (var i of inner) {
        finalArray.push(i);
      }
    }
  }
  return(finalArray);
}