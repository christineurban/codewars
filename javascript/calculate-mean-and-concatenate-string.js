// https://www.codewars.com/kata/56f7493f5d7c12d1690000b6

function mean(lst){
  var num = 0.0;
  var str = ""; 
  
  for (var char of lst) {
    if (parseInt(char) == char) {
      num += parseInt(char);
    } else {
      str += char;
    }
  }
  return([num/10, str]);
}
