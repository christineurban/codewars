// https://www.codewars.com/kata/the-highest-profit-wins

function minMax(arr){
  
  var min = arr[0];
  var max = arr[0];
  
  for (var i = 1; i < arr.length; i++) {
      if (arr[i] > max) {
      max = arr[i];
      };
      if (arr[i] < min) {
      min = arr[i];
      };
  };
   
  return [min, max];
};