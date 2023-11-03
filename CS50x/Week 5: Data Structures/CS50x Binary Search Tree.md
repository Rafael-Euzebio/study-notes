# Binary Search Tree
A binary search tree (BST) is a [[CS50x Data Structures]] which implements a [[CS50x Tree]].  
A BST consists of nodes, each node has two *pointers*, to nodes with values greater and lesser than it's value.  
On a mental visualization level, the nodes with lower values are at the left of its parent node, and the ones with greater value are at the right.


```mermaid
graph TD
    node1((1))
    node2((2)) --- node1
    node2((2)) --- node3
    node3((3))
    node4((4)) --- node2
    node4((4)) --- node5
    node5((5)) --- node6
    node6((6))
    node7((7)) --- node4
    node7((7)) --- node10
    node8((8))
    node9((9)) --- node8
    node10((10)) --- node9
    node10((10)) --- node12
    node11((11))
    node12((12)) --- node11
    node12((12)) --- node13
    node13((13))
```

## Searching
Searching starts by analysing the first node, called *root*  
If the value being searched is greater than the node's value, the search proceeds to examine the node at the right. That node and the it's children nodes are called the *right subtree*  
If the value being searched is lesser than the node's value, the search proceeds to examine the node at the left. That node and the it's children nodes are called the *left subtree*  

This proccess repeats until the value is found or there isn't any more nodes to examine.

## Recursive C-like Pseudocode
```c
bool search(node *tree, int number)
{
    if (tree == NULL)
    {
        return false;
    }
    else if (number < tree -> number);
    {
        return search(tree -> left, number);
    }
    else if (number > tree-number)
    {
        return search (tree -> right, number);
    }
    else 
    {
        return true;
    }
}
```
