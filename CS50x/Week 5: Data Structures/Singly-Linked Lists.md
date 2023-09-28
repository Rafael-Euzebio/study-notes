# Singly Linked Lists
A singly-linked list is a data structure of a linear collection of elements. The elements are not stored sequentially in memory, like and *array*, instead, each element points to the address of the next one.

## Structure
A singly-linked list is made of *nodes*, each node has a *data* and a *next* field  

`data` = the value stored in that node
`next` =  the address of the next node

## Use
Lists are a simple data structure that can be used to implement many *Abstract Data Types*, like [[Stack]] and [[Queue]]

## Example
We start by creating the structure of a node

```c
typedef struct node
{
    int number;
    struct node *next;
} node;
```

### Inserting Nodes
To insert a node we need to:  
1. Allocate memory for that node
2. Setting it's `next` field to `NULL`
3. Return the address of that node. In case of a *root* node, that address will be stored in a variable in `main` function for further use.

```c
int main()
{
    node *root = CreateNode();
}

node *CreateNode()
{
    node *new_node = malloc(sizeof(node));
    
    new_node -> next = NULL;
    return new_node;
}
```

#### Tail Insert
Tail Insert refers to a linked list which new nodes and values are inserted at the very end, one after the other.  
The steps to do that are:
1. Iterate through all nodes, starting at the root. 
2. Check if current node points to a `NULL` value
    - If current node pointers to another node, set current node to `next`
3. Create new node
4. Insert `value` in current node


```c
void InsertValue(node *root, int number)
{
    node *current_node = root;

    while(current_node -> next != NULL)
    {
        current_node = current_node -> next;
    }

    current_node -> next = CreateNode();
    current_node -> number = number;
}
```

The disadvange of Tail Insert is that adding new nodes is always linear time complexity $O(n)$

### Head Insert
Head Insert refers to a linked list which new nodes are inserted at the begginging at the list. New nodes coming before old ones.  
To do that it is necessary to keep changing the root pointer to the new node after every insertion.  
The steps to do that are:
1. Create a new node
2. Fill the `value` field of the new node
3. Point from new node to current root node
4. Change `root` pointer to point to new node (new root).

```c
void InsertValue(node **root, int number)
{
    node *new_node = CreateNode();
    new_node -> number = number;
    new_node -> next = *root; 
    *root = new_node;
}
```
The vantage of Head Insert is that inserting a new node is always constant time complexity $O(1)$ 

### Searching
A linked list cannot be searched with Binary Search or any other search algorithm other than Linear Search. There's no pointer to an arbitrary position of the list. It must be searched from the beggining to the end

1. Iterate through all the nodes
2. Check if the value being searched for is in the current node
    - If it isn't, set the current node as the next one
3. If reaches a nodes that pointers to `NULL`, value isn't in the list.

## Pros and Cons
A linked list can have values added to it without having to worry about enough memory being allocated in advance, unlike arrays, which must be reallocated to store more values than it size allows.
