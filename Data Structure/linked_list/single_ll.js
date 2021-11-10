"use strict";

class Node {
  constructor(data = null, next = null) {
    this.data = data;
    this.next = next;
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

class SingleLinkedList {
  constructor() {
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

    let result = curr.data;
    while (curr.next) {
      curr = curr.next;
      result += ` --> ${curr.data}`;
    }
    console.log(result);
  }

  /**
   * Insert a new value to the beginning of the linked list
   * @param {any types} value
   */
  insertAtBeginning(value) {
    this.length += 1;
    const newNode = new Node(value, this.head);
    this.head = newNode;
  }

  /**
   * Insert a new value to the end of the linked list
   * @param {any types} value
   */
  insertAtEnd(value) {
    this.length += 1;
    const newNode = new Node(value, null);

    // Handle empty linked list
    if (this.head === null) {
      this.head = newNode;
      return;
    }

    // Handle regular case
    let curr = this.head;
    while (curr.next) {
      curr = curr.next;
    }
    curr.next = newNode;
  }

  /**
   * Insert a new value at a specified index to the linked list
   * @param {any types} value
   * @param {Number} index
   */
  insertAt(value, index) {
    if (index > this.length || index < 0)
      throw new Error("Invalid index (out of bound");

    const newNode = new Node(value, null);
    let curr = this.head;

    if (index === 0) {
      this.insertAtBeginning(value);
      return;
    }

    // We want to stop at the position right before the desired index
    for (let i = 0; i < index - 1; i++) {
      curr = curr.next;
    }

    newNode.next = curr.next;
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
      this.length--;
      return this.length;
    }

    // Need to stop at the prev node
    while (curr.next) {
      if (curr.next.data === value) {
        curr.next = curr.next.next;
        this.length--;
        return this.length;
      }

      curr = curr.next;
    }

    return -1;
  }

  /**
   * Remove a node at the given index from the linked list
   * @param {Number} index
   * @returns 0 if successfully removed the node, -1 otherwise.
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
      this.length -= 1;
      return this.length;
    }

    // Handle regular case
    for (let i = 0; i < index - 1; i++) {
      curr = curr.next;
    }

    curr.next = curr.next.next ? curr.next.next : null;
    this.length -= 1;
    return this.length;
  }

  /**
   * Find the provided data in the linked list
   * @param {any types} value
   * @returns A boolean: true if data is found, false otherwise.
   */
  find(value) {
    let curr = this.head;

    // Handle empty case
    if (!curr) return false;

    while (curr.next) {
      if (curr.data === value) {
        return true;
      }
      curr = curr.next;
    }

    return false;
  }
}

/*------- TESTING -----------*/
const mySingleLL = new SingleLinkedList();
mySingleLL.insertAtBeginning(1);
mySingleLL.insertAtBeginning(2);
mySingleLL.insertAtBeginning(3);
mySingleLL.insertAtEnd("end");
mySingleLL.print();
mySingleLL.insertAt("insertAt", 0);
mySingleLL.print();
mySingleLL.removeAt(3);
mySingleLL.print();
