// https://www.codewars.com/kata/two-to-one

function longest(s1, s2) {
  
  var chars = "abcdefghijklmnopqrstuvwxyz";
  var s1s2 = s1 + s2;
  var letter = "";
  var match = "";
  var sorted = "";
 
  for (var i = 0; i < chars.length; i++) {
        // put current alphabetical character in var match
        match = chars[i];
    for (var j = 0; j < s1s2.length; j++) { 
        // check if string has letter of alphabet, and if so, put in var letter
        if (s1s2[j] == chars[i]) {
            letter = chars[i];
        };  
    };
    // only add to answer if alphabetical character appears once (stops duplicates)
    if (match == letter) {
        sorted += letter;
        };
  }; 
  return sorted;
}