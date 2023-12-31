# Tree
A tree is an [Abstract Data Type](./CS50x_Abstract-Data-Type.md) that represents an hierachical tree with many nodes. Each node is connected to any number of *children* nodes, but must have exactly only one *parent* node. Except for the *root* node, which has no parent

## Use
Trees are widely used to represent heierachical data, a common example are *file systems*. Each folder has many subfolders, but only one parent folder, and they all come from the *root* (`C:` in Windows or `/` in Linux)

## Operations
- Enumerating all the items
- Enumerating a section of a tree
- Searching for an item
- Adding a new item at a certain position on the tree
- Deleting an item
- Pruning: Removing a whole section of a tree
- Grafting: Adding a whole section to a tree
- Finding the root for any node
- Finding the lowest common ancestor of two nodes

```mermaid
graph TD
    node((root)) --> child1
    node((root)) --> child2
    child1((node)) --> child3
    child1((node)) --> child4
    child2((node)) --> child5
    child2((node)) --> child6
    child2((node)) --> child7((node))
    child3((node)) --> child8((node))
    child4((node))
    child5((node))
    child6((node))
```
