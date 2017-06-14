// https://www.codewars.com/kata/vasya-clerk

function tickets(peopleInLine){
  var vasya25 = 0;
  var vasya50 = 0;
  var vasya100 = 0;
  
  for (var i = 0; i <= peopleInLine.length; i++) {
    if (peopleInLine[i] == 25) {
        vasya25 += 1;
    } else if (peopleInLine[i] == 50) {
        if (vasya25 >= 1) {
            vasya50 += 1;
            vasya25 -= 1;
        } else {
            return "NO";
            break;
        };
    } else if (peopleInLine[i] == 100) {
        if (vasya50 >= 1 && vasya25 >= 1) {
            vasya50 -= 1;
            vasya25 -= 1;
        } else if (vasya50 == 0 && vasya25 >= 3) {
            vasya25 -= 3;
        } else {
            return "NO";
            break;
        };
    } else {
        return "YES";
    };
  }; 
};