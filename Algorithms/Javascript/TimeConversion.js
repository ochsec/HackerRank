/**
 * Given a time in AM/PM format, convert it to military (24-hour) time.
 * Input Format: A single string containing a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM), where 01 <= hh <= 12.
 * Output Format: Convert and print the given time in 24-hour format, where 00 <= hh <= 23.
 * Sample Input: 07:05:45PM
 * Sample Output: 19:05:45
 */

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

function main() {
    var time = readLine();
    var hr = Number(time.split(':')[0]);
    var min = time.split(':')[1];
    var sec = time.split(':')[2];
    if (isPm(time)) {
        hr = hr < 12 ? hr + 12 : hr;
    } else {
        hr = hr == 12 ? '00' : hr
    }
    console.log(pad(hr) + ':' + min + ':' + sec.replace(/[^0-9]/g, ''));
}

function isPm(str) {
    return str.split(':')[2].toLowerCase().replace(/[^a-z]/g, '') === 'am' ? false : true;
}

function pad(num) {
    return num.toString().length < 2 ? '0' + num : num;
}