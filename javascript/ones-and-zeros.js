// https://www.codewars.com/kata/ones-and-zeros

const binaryArrayToNumber = arr => {
  var binary = 0
  var counter = 1
  for (var i = arr.length - 1; i >= 0; i--) {
    binary += arr[i] * counter;
    counter += counter;
  }
  return binary;
};
