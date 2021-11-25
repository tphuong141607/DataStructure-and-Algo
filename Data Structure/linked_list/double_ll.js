"use strict";

class Node {
  constructor(data = null, next = null, prev = null) {
    this.data = data;
    this.next = next;
    this.prev = prev;
  }
}

/***
  LinkedList Operations:
      1. print(): access each element of the linked list and display them
      2. insertAtBeginning(value): add a new node to the beginning 
      2. insertAtEnd(value): add a new node to the end 
      3. insertAt(value, index): add a new node at a specified index   
      5. removeByValue(value): remove a node 
      6. removeAt(index): remove a node at a specified index   
      7. find(value): find a node 
  */

class DoubleLinkedList {
  constructor() {
    this.tail = null;
    this.head = null;
    this.length = 0;
  }

  /**
   * Print the linked list in a concise and clean string representation
   * @param {any types} value
   */
  print() {
    let curr = this.head;
    if (!this.head) {
      console.log("Empty LinkedList");
      return;
    }

    let result = `Head: ${this.head.data}, Tail: ${this.tail.data}, length: ${this.length} \n${curr.data}`;
    while (curr.next) {
      curr = curr.next;
      result += ` <--> ${curr.data}`;
    }
    console.log(result);
  }

  /**
   * Insert a new value to the beginning of the linked list
   * @param {any types} value
   */
  insertAtBeginning(value) {
    this.length += 1;
    const newNode = new Node(value, this.head, null);

    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }

    this.head.prev = newNode;
    this.head = newNode;
  }

  /**
   * Insert a new value to the end of the linked list
   * @param {any types} value
   */
  insertAtEnd(value) {
    this.length += 1;
    const newNode = new Node(value, null, null);

    // Handle empty linked list
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }

    // Handle regular case
    this.tail.next = newNode;
    newNode.prev = this.tail;
    this.tail = newNode;
  }

  /**
   * Insert a new value at a specified index to the linked list
   * @param {any types} value
   * @param {Number} index
   * Improvement (TODO): only search half the list
   */
  insertAt(value, index) {
    if (index > this.length || index < 0)
      throw new Error("Invalid index (out of bound");

    const newNode = new Node(value, null, null);

    // Handle removing node at index 0
    if (index === 0) {
      this.insertAtBeginning(value);
      return;
    }

    if (index === this.length) {
      this.insertAtEnd(value);
      return;
    }

    this.length++;
    const midPoint = Math.floor(this.length / 2);
    let curr;

    if (index <= midPoint) {
      curr = this.head;

      // We want to stop at the position right before the desired index
      for (let i = 0; i < index - 1; i++) {
        curr = curr.next;
      }
    } else {
      curr = this.tail;

      for (let i = this.length; i > index + 1; i--) {
        curr = curr.prev;
      }
    }

    newNode.next = curr.next;
    newNode.prev = curr;
    curr.next.prev = newNode;
    curr.next = newNode;
  }

  /**
   * Remove a node with the given value from the linked list
   * @param {any types} value
   * @returns the linked list length if successfully removed the node, -1 otherwise.
   */
  removeByValue(value) {
    let curr = this.head;

    if (curr === null) return -1;

    if (curr.data === value) {
      this.head = curr.next;
      this.head.prev = null;

      this.length += 1;
      return this.length;
    }

    // Need to stop at the prev node
    while (curr.next) {
      if (curr.next.data === value) {
        // Update this.tail value
        if (curr.next === this.tail) {
          this.tail = curr;
        }

        // remove operation
        curr.next = curr.next.next;
        if (curr?.next?.next?.prev) {
          curr.next.next.prev = curr;
        }
        this.length -= 1;
        return this.length;
      }

      curr = curr.next;
    }
    return -1;
  }

  /**
   * Remove a node at the given index from the linked list
   * @param {Number} index
   * @returns the current if successfully removed the node, -1 otherwise.
   */
  removeAt(index) {
    let curr = this.head;

    // Check for valid index
    if (index < 0 || index > this.length)
      throw new Error("Invalid index (out of bound");

    // return -1 if linked list is empty
    if (curr === null) return -1;

    // Handle remove the 1st node
    if (index === 0) {
      this.head = curr.next;
      curr.next.prev = null;
      this.length -= 1;
      return this.length;
    }

    // Handle remove the last node
    if (index === this.length) {
      this.tail = this.tail.prev;
      this.tail.next = null;
      this.length -= 1;
      return this.length;
    }

    // Handle regular case (we could improve this by only check half the linked list)
    for (let i = 0; i < index - 1; i++) {
      curr = curr.next; // the node before the one we want to remove
    }

    curr.next = curr.next.next ? curr.next.next : null;
    if (curr?.next?.next?.prev) {
      curr.next.next.prev = curr;
    }

    this.length -= 1;
    return this.length;
  }

  /**
   * Find the provided data in the linked list
   * @param {any types} value
   * @returns an index if found, -1 otherwise.
   */
  find(value) {
    let curr = this.head;

    // Handle empty case
    if (!curr) return -1;
    let count = 0;

    while (curr.next) {
      if (curr.data === value) {
        return count;
      }
      count += 1;
      curr = curr.next;
    }
    return -1;
  }
}

/*------- TESTING -----------*/
// const myDoubleLL = new DoubleLinkedList();
// myDoubleLL.insertAtBeginning(1);
// myDoubleLL.insertAtBeginning(2);
// myDoubleLL.insertAtBeginning(3);
// myDoubleLL.print();
// myDoubleLL.insertAtEnd("end");
// myDoubleLL.print();
// myDoubleLL.insertAt("insertAt", myDoubleLL.length);
// myDoubleLL.print();
// myDoubleLL.removeAt(0);
// myDoubleLL.print();
// console.log(myDoubleLL.find(1));

export default DoubleLinkedList;
