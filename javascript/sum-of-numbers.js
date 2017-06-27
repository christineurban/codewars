// https://www.codewars.com/kata/beginner-series-number-3-sum-of-numbers

function GetSum( a,b )
{
   var sum = 0;
   
   if (a == b) {
       return a;
   } else if (a < b) {
       for (var i = a; i <= b; i++) {
       sum += i;
       };
   } else {
       for (var j = b; j <= a; j++) {
       sum += j;
       };
   };
   
   return sum;  
   
}