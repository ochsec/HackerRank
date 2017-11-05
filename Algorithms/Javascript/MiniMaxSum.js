// https://www.hackerrank.com/challenges/mini-max-sum/problem

process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

const main = () => {
    const ordered = readLine().split(' ').map(Number).sort();    
    const min = ordered.slice(0, 4).reduce((a, b) => a + b);
    const max = ordered.slice(1, 5).reduce((a, b) => a + b);
    
    console.log(`${min} ${max}`);
}
