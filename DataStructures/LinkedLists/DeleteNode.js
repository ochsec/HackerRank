// https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

const SinglyLinkedListNode = class {
    constructor(nodeData) {
        this.data = nodeData;
        this.next = null;
    }
};

const SinglyLinkedList = class {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    insertNode(nodeData) {
        const node = new SinglyLinkedListNode(nodeData);

        if (this.head == null) {
            this.head = node;
        } else {
            this.tail.next = node;
        }

        this.tail = node;
    }
};

function printSinglyLinkedList(node, sep, ws) {
    while (node != null) {
        ws.write(String(node.data));

        node = node.next;

        if (node != null) {
            ws.write(sep);
        }
    }
}

/*
 * Complete the 'deleteNode' function below.
 *
 * The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
 * The function accepts following parameters:
 *  1. INTEGER_SINGLY_LINKED_LIST llist
 *  2. INTEGER position
 */

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */

function deleteNode(head, position, first = true) {
    // Write your code here
    // Write your code here
    if (!head) {
        return null;
    }
    
    if (position === 0 && first) {
        return head.next;
    }
    
    if (position === 1) {
        let prevNode = head;
        let currNode = head.next;
        let nextNode = currNode.next;
        prevNode.next = nextNode;
        return prevNode;
    }
    
    head.next = deleteNode(head.next, position - 1, false);
    return head;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const llistCount = parseInt(readLine(), 10);

    let llist = new SinglyLinkedList();

    for (let i = 0; i < llistCount; i++) {
        const llistItem = parseInt(readLine(), 10);
        llist.insertNode(llistItem);
    }

    const position = parseInt(readLine(), 10);

    let llist1 = deleteNode(llist.head, position);

    printSinglyLinkedList(llist1, " ", ws)
    ws.write("\n");

    ws.end();
}
