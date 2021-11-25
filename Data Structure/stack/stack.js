"use strict";

class Stack {
  constructor() {
    this.items = [];
  }

  // add an item to the stack
  push(item) {
    this.items.push(item);
  }

  // remove and return the removed item
  pop(item) {
    if (this.items.length > 0) {
      return this.items.pop();
    }
  }

  // view the last item
  peek() {
    return this.items[this.items.length - 1];
  }

  isEmpty() {
    return this.items.length === 0;
  }

  size() {
    return this.items.length;
  }

  clear() {
    this.items = [];
  }

  print() {
    console.log(this.items);
    console.log(`The item at the top of the stack is: ${this.peek()}`);
    console.log(
      `Our stack is ${
        this.isEmpty() ? "" : "not"
      } empty; It has length ${this.size()}`
    );
  }
}

/*------- TESTING -----------*/
let stack = new Stack();
stack.push("h");
stack.push("a");
stack.push("p");
stack.push("p");
stack.push("y");
stack.print();

console.log("--------");
stack.pop();
stack.pop();
stack.print();

console.log("--------");
stack.clear();
stack.print();
