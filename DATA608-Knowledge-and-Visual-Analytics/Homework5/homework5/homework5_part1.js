function reverseString(){
var str = window.prompt("Please enter a word to be printed in reverse");
var splitstr = str.split(""); // split string into array of chars

var reversestr = splitstr.reverse(); // reserve array

var finalString = reversestr.join(""); // re-assemble array into string
return finalString;}
window.alert("Reversed String: " + reverseString())


function printTimeTable(){
// compute the first 20 multiples of the inputted number
var number = window.prompt("Please enter a number to print 5 x 4 of multiples of that number");
var multiples = new Array(20);
for (var i = 0; i < 20; i++) { multiples[i] = number*(i+1); }
document.write("<table>");
var ctr = 0 // keep track of the multiples array during the loop
for(var i = 0; i < 5; i++){
document.write("<tr>");
	for(var j = 0; j < 4; j++){		
		document.write("<td>" + multiples[ctr] + "</td>");
		ctr++;
	}
document.write("</tr>");
}
document.write("</table>");
}
printTimeTable();