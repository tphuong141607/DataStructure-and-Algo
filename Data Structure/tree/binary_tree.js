"use strict";
/*
 * Basic operations on a BST
 * Create: creates an empty tree.
 * Insert: insert a node in the tree.
 * Search: Searches for a node in the tree.
 * Delete: deletes a node from the tree.
 * BFS: Level Order Traversal
 * DFS:
 *  Inorder: in-order traversal of the tree.
 *  Preorder: pre-order traversal of the tree.
 *  Postorder: post-order traversal of the tree.
 */

import Queue from "../queue/queue.js";

class BTSNode {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  /**
   * @param {BTSNode} root
   */
  constructor(root = null) {
    this.root = root;
  }

  insert(data) {
    const newNode = new BTSNode(data);

    // Handle when the BTS is empty
    if (!this.root) {
      this.root = newNode;
      return;
    }

    // add newNode to the BTS
    this.insertNode(this.root, newNode);
  }

  /**
   * Add a new BTSNode to the tree by recursively traversing the tree
   * @param {BTSNode} currNode
   * @param {BTSNode} newNode
   */
  insertNode(currNode, newNode) {
    // Handle duplicates
    if (currNode.data === newNode.data) return;

    // add data to left subtree of the currNode
    if (newNode.data < currNode.data) {
      if (!currNode.left) {
        currNode.left = newNode;
      } else {
        this.insertNode(currNode.left, newNode);
      }
    }
    // add data to right subtree of the currNode
    else {
      if (!currNode.right) {
        currNode.right = newNode;
      } else {
        this.insertNode(currNode.right, newNode);
      }
    }
  }

  /**
   * Delete a node
   * 1. Delete node with no child
   * 2. Delete node with 1 child: change pointer
   * 3. Delete node with 2 children: re-blance
   *    3a. Option1: take the minimum value from the right subtree and use that as the new middle node
   *    3b. option2: take the maximum value from the left subtree, and use that as the new middle node
   */

  delete(data, currNode = null) {
    // Handle root removal
    if (!currNode) {
      this.root = this.delete(data, this.root);
      return;
    }

    if (data < currNode.data) {
      currNode.left = this.delete(data, currNode.left);
    } else if (data > currNode.data) {
      currNode.right = this.delete(data, currNode.right);
      // Found
    } else {
      // Case 1: leaf node
      if (!(currNode.left || currNode.right)) {
        currNode = null;
      }
      // Case 2: 1 child
      else if (!currNode.left) {
        currNode = currNode.right;
      } else if (!currNode.right) {
        currNode = currNode.left;
      }
      // Case 3: 2 children
      else {
        const minNode = this.findMin(currNode.right);
        currNode.data = minNode.data;
        currNode.right = this.delete(minNode.data, currNode.right);
      }
    }
    // This return value is important! If you don't return, currNode.left /currNode.right might receive undefined instead of the real node object
    return currNode;
  }

  findMax(currNode = this.root) {
    if (!currNode.right) {
      return currNode;
    }

    return this.findMax(currNode.right);
  }

  findMin(currNode = this.root) {
    if (!currNode.left) {
      return currNode;
    }

    return this.findMax(currNode.left);
  }

  search(data, currNode = this.root) {
    if (!this.root) return false;
    if (currNode.data === data) return true;
    if (data < currNode.data && currNode.left)
      return this.search(data, currNode.left);
    if (data > currNode.data && currNode.right)
      return this.search(data, currNode.right);
    return false;
  }

  // left, node, right
  inorderDFS(currNode = this.root) {
    if (!this.root) return;
    let result = [];
    if (currNode.left) {
      result.push(...this.inorderDFS(currNode.left));
    }
    result.push(currNode.data);
    if (currNode.right) {
      result.push(...this.inorderDFS(currNode.right));
    }

    return result;
  }

  // node, left, right
  preorderDFS(currNode = this.root) {
    if (!this.root) return;
    const result = [];
    result.push(currNode.data);
    if (currNode.left) {
      result.push(...this.preorderDFS(currNode.left));
    }
    if (currNode.right) {
      result.push(...this.preorderDFS(currNode.right));
    }

    return result;
  }

  // left, right, node
  postorderDFS(currNode = this.root) {
    if (!this.root) return;
    let result = [];
    if (currNode.left) {
      result.push(...this.postorderDFS(currNode.left));
    }
    if (currNode.right) {
      result.push(...this.postorderDFS(currNode.right));
    }

    result.push(currNode.data);

    return result;
  }

  BFS() {
    const queue = new Queue();
    const result = [];
    let level = 0;

    // Handle when the BTS is empty
    if (!this.root) return [result, level];

    queue.enqueue(this.root);
    level += 1;

    while (!queue.isEmpty()) {
      const currNode = queue.dequeue();
      let newLevel = false;
      result.push(currNode.data);

      if (currNode.left) {
        queue.enqueue(currNode.left);
        newLevel = true;
      }
      if (currNode.right) {
        queue.enqueue(currNode.right);
        newLevel = true;
      }

      if (newLevel) level += 1;
    }
    return [result, level];
  }
}
/*------- TESTING -----------*/
const myBTS = new BinarySearchTree();

// Inserting
myBTS.insert(6);
myBTS.insert(3);
myBTS.insert(1);
myBTS.insert(4);
myBTS.insert(5);
myBTS.insert(7);
myBTS.insert(10);
myBTS.insert(2);

// Deleting
myBTS.delete(6);

/* 
                6

        3              7
    1       4               10
        2       5
            
*/

// Traversal
console.log("inorder: ", myBTS.inorderDFS());
console.log("preorder: 6 3 1 2 4 5 7 10", myBTS.preorderDFS());
console.log("postorder: 2 1 5 4 3 10 7 6", myBTS.postorderDFS());
console.log("BFS", myBTS.BFS()[0]);

// Searching
console.log(`Searching for 6: ${myBTS.search(6)}`);
console.log(`Searching for -1: ${myBTS.search(-1)}`);
console.log(`Searching for 10: ${myBTS.search(10)}`);
