"use strict";

/**
STEPs:
    1. Create a HashTable class with table and size initial properties
    2. Add a hash() function to transform keys into indices
    3. Add the add(), get(), and delete() methods 

Hash Table Operations:
    1. getHash(key): generate the hash code, aka hash function      O(len(key))
    2. add(key): Add the key-vale pair to our hash table            
    3. get(key): Get the value, given a key                         
    4. delete(key): Delete a key-value pair by key                  

Handling collisions:
    1. Chaining: Each spot in the array is 
        a. a linked list, whose value is pair [key,value] (linked list is better for delete operation O(1) compared to an array O(n))
        b. an array of pairs [key, value]. 
    2. Probing: Each spot in the array is a pair [key, value]. We simply try to find an empty spot to store the new entry.
    Note: JS doesn't have tuple

*/

import DoubleLinkedList from "../linked_list/double_ll.js";

class HashTable {
  constructor(size = 10) {
    this.table = Array(size)
      .fill()
      .map(() => new DoubleLinkedList());
    this.size = size;
  }

  printHashTable() {
    for (let i = 0; i < this.size; i++) {
      console.log(i);
      this.table[i]?.print();
    }
  }

  /**
   * Convert each string char to its corresponding ASCII Decimal Code, then sum all ASCII decimal code.
   * Return the sum % size to get the corresponding array indice.
   * @param {String} keyString
   */
  getHash(keyString) {
    let sumCode = 0;
    for (let char of keyString) {
      sumCode += char.charCodeAt(0);
    }
    return sumCode % this.size;
  }

  /**
   * Add the key-value pair to the hash table
   * @param {String} key
   * @param {any} value
   */
  add(key, value) {
    // convert key to an appropriate array indice
    const indice = this.getHash(key);
    let found = false;

    const currLinkedList = this.table[indice];
    let currNode = currLinkedList.head;

    // if the currLinkedList is empty:
    if (!currNode) {
      currLinkedList.insertAtEnd([key, value]);
      // currLinkedList.print();
      return;
    }

    if (currNode.data[0] === key) {
      currNode.data[1] = value;
      found = true;
    }

    // if key exists, replace the old value with the new value
    while (currNode.next) {
      currNode = currNode.next;
      if (currNode.data[0] === key) {
        console.log(currNode.data[0], key);
        currNode.data[1] = value;
        found = true;
        break;
      }
    }

    // if key doesn't exist, simply add to the table
    if (!found) {
      currLinkedList.insertAtEnd([key, value]);
    }
  }

  /**
   * Return the key-value pair from the hash table if found. Return -1 otherwise.
   * @param {String} key
   */
  get(key) {
    const indice = this.getHash(key);
    let result = -1;

    const currLinkedList = this.table[indice];
    let currNode = currLinkedList.head;

    if (currNode.data[0] === key) {
      result = currNode.data;
    }

    // if key exists, replace the old value with the new value
    while (currNode.next) {
      currNode = currNode.next;
      if (currNode.data[0] === key) {
        result = currNode.data;
        break;
      }
    }

    console.log(result);
    return result;
  }

  /**
   * Delete the key-value pair from the hash table. Return -1 if delete unsuccessful.
   * @param {String} key
   */
  delete(key) {
    const indice = this.getHash(key);
    const currLinkedList = this.table[indice];
    let currNode = currLinkedList.head;

    // if the currLinkedList is empty:
    if (!currNode) {
      return -1;
    }

    // if head is what we want to remove
    if (currNode.data[0] === key) {
      removeAt(0);
    }

    // Need to stop at the prev node
    while (currNode.next) {
      if (currNode.next.data[0] === key) {
        // Update this.tail value
        if (currNode.next === this.tail) {
          this.tail = currNode;
        }

        // remove operation
        currNode.next = currNode.next.next;
        if (currNode?.next?.next?.prev) {
          currNode.next.next.prev = currNode;
        }
        this.length -= 1;
        break;
      }

      currNode = currNode.next;
    }
  }
}

/*------- TESTING -----------*/
const testHashTable = function (arrInput) {
  const hashTable = new HashTable();

  // Add data to hashTable
  for (let i = 0; i < arrInput.length; i++) {
    const currEntry = arrInput[i];
    hashTable.add(currEntry[0], currEntry[1]);
  }
  hashTable.printHashTable();

  // Update value
  hashTable.add("salad", 5);

  // Get value
  hashTable.get("salad");

  // Delete value
  hashTable.delete("salad");
  hashTable.get("salad");
  hashTable.get("pho");
};

const mealQuanity = [
  ["pho", 2],
  ["steamy bun", 5],
  ["spicy pork", 4],
  ["hawaiian pizza", 1],
  ["cheese burger", 9],
  ["salad", 6],
];

testHashTable(mealQuanity);
