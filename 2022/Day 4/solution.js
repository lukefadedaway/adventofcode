function getAnswerPart1(x) {
    var ranges = x.split(",");
    var rangeOne = ranges[0].split("-");
    var rangeTwo = ranges[1].split("-");
    if(parseInt(rangeOne[0]) >= parseInt(rangeTwo[0]) && parseInt(rangeOne[1]) <= parseInt(rangeTwo[1])) return 1;
    if(parseInt(rangeTwo[0]) >= parseInt(rangeOne[0]) && parseInt(rangeTwo[1]) <= parseInt(rangeOne[1])) return 1;
    return 0;
};

function getAnswerPart2(x) {
    var ranges = x.split(",");
    var rangeOne = ranges[0].split("-");
    var rangeTwo = ranges[1].split("-");
    if(parseInt(rangeOne[0]) >= parseInt(rangeTwo[0]) && parseInt(rangeOne[0]) <= parseInt(rangeTwo[1])) return 1;
    if(parseInt(rangeTwo[0]) >= parseInt(rangeOne[0]) && parseInt(rangeTwo[0]) <= parseInt(rangeOne[1])) return 1;
    if(parseInt(rangeOne[1]) >= parseInt(rangeTwo[0]) && parseInt(rangeOne[1]) <= parseInt(rangeTwo[1])) return 1;
    if(parseInt(rangeTwo[1]) >= parseInt(rangeOne[0]) && parseInt(rangeTwo[1]) <= parseInt(rangeOne[1])) return 1;
    return 0;
};

var args = process.argv.slice(2);
var fs = require('fs');
var path = process.cwd();
var buffer = fs.readFileSync(path + "/" + args[0]);
var inputtext = buffer.toString();
var myArray = inputtext.split("\n");

var answerPart1 = 0, answerPart2 = 0;
myArray.forEach(function(x) {
    answerPart1 += getAnswerPart1(x);
    answerPart2 += getAnswerPart2(x);
});
console.log("Part 1:\n" + answerPart1);
console.log("Part 2:\n" + answerPart2);