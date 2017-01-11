// Day 1: Standard Deviation
// https://www.hackerrank.com/challenges/s10-standard-deviation

// Day 1: Standard Deviation
// https://www.hackerrank.com/challenges/s10-standard-deviation

function processData(input) {
    //Enter your code here
    let lines = input.split('\n');
    let N = parseInt(lines[0]);
    let vals = lines[1].split(' ').map((num) => {
        return parseInt(num);    
    });
 
    var getSum = new Promise(
        function(resolve, reject) {
            var s = sum(vals);
            resolve(s);
        }
    );
    
    getSum.then(function(sum) {
        return sum/N;
    }).then(function(mean) {
        return getSqDeviations(mean, vals);
    }).then(function(sqDevs) {
        return standardDev(N, sqDevs);
    }).then(function(sd) {
        console.log(sd.toFixed(1));
    })
      .catch(function(e) {
        console.log(e); 
    });
}

var sum = (nums) => {
    return nums.reduce((a, b) => {
        return a + b;        
    }, 0);    
};

var getSqDeviations = (mean, vals) => {
    return sqDevs = vals.map((val) => {
        return devSquared(mean, val);    
    });
};

var devSquared = (mean, val) => {
    var diff = val - mean;
    return diff * diff;    
};

standardDev = (N, sqDevs) => {
    this.sumSqDevs = sum(sqDevs);
    return Math.sqrt(this.sumSqDevs/N);    
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

