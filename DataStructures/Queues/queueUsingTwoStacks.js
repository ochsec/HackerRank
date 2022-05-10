function processData(input) {
    //Enter your code here
    const ops = input.split('\n')
        .filter((x, index) => index != 0)
        .map(y => y.split(' ')
            .map(z => parseInt(z)))
    let Q = [] // Queue

    ops.forEach(op => {
        if (op[0] == 1) {
            // Enqueue
            Q.push(op[1])
        } else if (op[0] == 2) {
            // Dequeue
            Q.shift()
        } else {
            console.log(Q[0])            
        }
    })
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
