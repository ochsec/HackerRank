// Day 1: Quartiles
// https://www.hackerrank.com/challenges/s10-quartiles

function processData(input) {
    //Enter your code here
    let lines = input.split('\n');
    let vals= lines[1].split(' ').map((val) => {
        return parseInt(val); 
    });
    
    let X = median(vals);
    let lowerVals = smallerOrEqualToMedian(vals, X);
    let L = median(lowerVals);
    let upperVals = equalToOrGreaterThanMedian(vals, X);
    let U = median(upperVals);
    console.log(L);
    console.log(X);
    console.log(U);    
} 

var median = (nums) => {
    let sorted = nums.sort(sortNums);
    let len = sorted.length;
    
    if (len % 2 !== 0) {
        return sorted[Math.floor(len / 2)];     
    }
    
    return (sorted[Math.floor(len / 2) - 1] + sorted[Math.floor(len / 2)]) / 2
};

var sortNums = (a, b) => {
    return a - b;
};

function smallerOrEqualToMedian(vals, X) {
    return vals.filter((val) => {
        return val < X;     
    });           
};

function equalToOrGreaterThanMedian(vals, X) {
    return vals.filter((val) => {
        return val > X;         
    });      
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
