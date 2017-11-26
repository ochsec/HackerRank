// https://www.hackerrank.com/challenges/2d-array/problem

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

function main() {
    var arr = [];
    for(arr_i = 0; arr_i < 6; arr_i++){
       arr[arr_i] = readLine().split(' ');
       arr[arr_i] = arr[arr_i].map(Number);
    }
    
    const vectors = createVectors(arr);
    const sums = vectors.map(v => v.reduce(sum));
    const max = sums.sort((a, b) => b - a)[0];
    print(max);
}

const print = (entity) => console.log(entity);

const createVectors = (arr) => {
    let vectors = [];
    for (let i = 0; i < arr.length -2; i++) {
        for (let j = 0; j < arr[0].length - 2; j++) {
            let v = [];
            v.push(arr[i][j]);
            v.push(arr[i][j+1]);
            v.push(arr[i][j+2]);
            v.push(arr[i+1][j+1]);
            v.push(arr[i+2][j]);
            v.push(arr[i+2][j+1]);
            v.push(arr[i+2][j+2]);
            vectors.push(v);
        }
    }
    
    return vectors;
}

const sum = (total, num) => total + num;