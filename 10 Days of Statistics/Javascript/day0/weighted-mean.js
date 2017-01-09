// Day 0: Weighted Mean
// https://www.hackerrank.com/challenges/s10-weighted-mean

function processData(input) {
    //Enter your code here
    let lines = input.split('\n');
    let vals = lines[1].split(' ').map((val) => {
        return parseInt(val);    
    });
    let weights = lines[2].split(' ').map((w) => {
        return parseInt(w);    
    });
    
    console.log(wMean(vals, weights).toFixed(1));
} 

var wMean = (vals, weights) => {
    var sum = 0;
    var div = 0;
    
    for (var i = 0; i < vals.length; i++) {
        sum += vals[i] * weights[i];
        div += weights[i];
    }
    
    return sum / div;
};

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
