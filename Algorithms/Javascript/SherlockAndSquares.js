//Watson gives two integers (A and B) to Sherlock and asks if he can count the number of square integers between A and B (both inclusive).

//Note: A square integer is an integer which is the square of any integer. For example, 1, 4, 9, and 16 are some of the square integers as 
//they are squares of 1, 2, 3, and 4, respectively.

//Input Format 
//The first line contains T, the number of test cases. T test cases follow, each in a new line. 
//Each test case contains two space-separated integers denoting A and B.

//Output Format 
//For each test case, print the required answer in a new line.

//Constraints
//1 <= T <= 100
//1 <= A <= B <= 10^9

//Sample Input
//2
//3 9
//17 24

//Sample output
//2 
//0

//Explanation 
//Test Case #00: In range [3,9], 4 and 9 are the two square numbers. 
//Test Case #01: In range [17,24], there are no square numbers.

function processData(input) {
    var inputLines = input.split('\n');
    for (var i = 0; i < Number(inputLines[0]) ; i++) {
        var countOfSquares = 0;
        var firstSquareRoot = 0;
        var endpoints = inputLines[i + 1].split(' ');
        var start = Number(endpoints[0]);
        var end = Number(endpoints[1]);
        for (var j = start; j <= end; j++) {
            if (Math.sqrt(j) % 1 === 0) {
                firstSquareRoot = Math.sqrt(j);
                countOfSquares++;
                break;
            }
        }
        if (firstSquareRoot === 0) {
            console.log(0);
        } else {
            var k = firstSquareRoot + 1;
            while (k * k <= end) {
                countOfSquares++;
                k++;
            }
            console.log(countOfSquares);
        }
    }
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
