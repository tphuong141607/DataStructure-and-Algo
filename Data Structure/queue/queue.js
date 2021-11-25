"use strict";

import DoubleLinkedList from "../linked_list/double_ll.js";

class Queue {
  constructor() {
    this.items = new DoubleLinkedList();
  }

  enqueue(item) {
    this.items.insertAtBeginning(item);
  }

  dequeue() {
    const tail = this.items.tail;
    const removed = this.items.removeAt(this.items.length - 1);
    return removed === -1 ? -1 : tail.data;
  }

  isEmpty() {
    return this.items.length === 0;
  }

  size() {
    return this.items.length;
  }

  print() {
    this.items.print();
  }
}

let myQueue = new Queue();

// Live's reverse form is evil. Kinda funny.
myQueue.enqueue("l");
myQueue.enqueue("i");
myQueue.enqueue("v");
myQueue.enqueue("e");

myQueue.print();
console.log(myQueue.dequeue());
console.log(myQueue.isEmpty(), myQueue.size());
myQueue.print();
