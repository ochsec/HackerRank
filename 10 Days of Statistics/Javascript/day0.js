// Day 0: Mean, Median, and Mode
// https://www.hackerrank.com/challenges/s10-basic-statistics

function processData(input) {
    //Enter your code here
    let lines = input.split('\n');
    let N = parseFloat(lines[0]);
    let nums = lines[1].split(' ').map((num) => {
        return parseFloat(num);    
    });
                           
    console.log(mean(N, nums));
    console.log(median(nums));
    console.log(mode(nums));
} 

var mean = (N, nums) => {
    this.sum = sum(nums);
    return this.sum / N;
};

var sum = (nums) => {
    return nums.reduce((a, b) => {
        return a + b;        
    }, 0);    
};

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

var mode = (nums) => {
    this.table = frequencies(nums);
    return findMaxFreq(this.table);
};

var frequencies = (numsArr) => {
    let sorted = numsArr.sort(sortNums);
    var max = 0;
    var prev = null;
    var table = {};
    var highest;
    
    sorted.forEach((val) => {
        if (!table[val]) {
            table[val] = 1;
        } else {
            table[val]++;    
        }
                
    }, this);
    
    return table;
};

var findMaxFreq = (table) => {
    var maxFreq = 0;
    var maxMode = null;
    
    for (var key in table) {
        if (maxMode === null) {
            maxMode = parseFloat(key);
        }
        
        if (table[key] > maxFreq) {
            maxFreq = parseInt(table[key]);
            maxMode = parseFloat(key);
        }
    }
    
    return maxMode;
}
 
process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
