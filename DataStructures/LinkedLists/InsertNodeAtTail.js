// https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
'use strict';

const SinglyLinkedListNode = class {
    constructor(nodeData) {
        this.data = nodeData;
        this.next = null;
    }
};

const SinglyLinkedList = class {
    constructor() {
        this.head = null;
    }

};

function printSinglyLinkedList(node, sep) {
    while (node != null) {
        console.log(String(node.data));

        node = node.next;

        if (node != null) {
            console.log(sep);
        }
    }
}

// Complete the insertNodeAtTail function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */
function insertNodeAtTail(head, data) {
    if (!head) {
        const head = new SinglyLinkedListNode(data);
        return head;    
    }
    
    insertNodeAtTail(head.next, data);
}

function main() {
    const llistCount = 5;

    let llist = new SinglyLinkedList();
    let listItems = [141, 302, 164, 530, 474];

    for (let i = 0; i < llistCount; i++) {
        const llistItem = listItems[i];
    	const llist_head = insertNodeAtTail(llist.head, llistItem);
      	llist.head = llist_head;
    }

    printSinglyLinkedList(llist.head, '\n');
}

main();