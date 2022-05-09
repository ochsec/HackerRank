function processData(input) {
    //Enter your code here
    const ops = input.split('\n')
        .filter((x, index) => index != 0)
        .map(y => y.split(' ')
            .map(z => parseInt(z)))
    let A = [] // Queue stack
    let B = [] // Dequeue stack
    output = [] // The numbers to return to be printed

    ops.forEach(op => {
        if (op[0] == 1) {
            // Enqueue
            if (A.length == 0) {
                while (B.length > 0) {
                    A.push(B.pop())
                }
            }
            A.push(op[1])
        } else if (op[0] == 2) {
            // Dequeue
            if (B.length == 0) {
                while (A.length > 0) {
                    B.push(A.pop())
                }
            }
            B.pop()
        } else {
            if (B.length == 0) {
                while (A.length > 0) {
                    B.push(A.pop())
                }
            }
            console.log(B[B.length - 1])            
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