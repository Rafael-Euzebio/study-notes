# Singly Linked Lists
A singly-linked list is a [[Linked Lists]] data structure, a linear collection of elements. The elements are not stored sequentially in memory, like and *array*, instead, each element points to the address of the next one.

## Structure
A singly-linked list is made of *nodes*, each node has a *data* and a *next* field  

`data` = the value stored in that node
`next` =  the address of the next node

## Example
We start by creating the structure of a node

```c
typedef struct node
{
    int data;
    struct node *next;
} node;
```

### Creating a Linked List
To create a linked list we first need to create our `root` node.

1. Allocate memory for that node
2. Set it's `next` field to `NULL`
3. Fill it's `data` field
4. Return it's address

```c
int main()
{
    node *root = CreateRoot();
}

node *CreateRoot(int value)
{
    node *root = malloc(sizeof(node));
    root -> next = NULL;
    root -> data  = value;

    return root;
}
```

### Inserting Nodes
#### Tail Insert
Tail Insert refers to a linked list which new nodes and values are inserted at the very end, one after the other.  
The steps to do that are:
1. Iterate through all nodes, starting at the root. 
2. Check if current node points to a `NULL` value
    - If current node pointers to another node, set current node to `next` and repeat
3. Create new node
    - We can use the earlier function `CreateRoot()` to do that. Each node is a "root" to the next one

```c
void InsertNode(node *root, int value)
{
    node *current_node = root;

    while(current_node -> next != NULL)
    {
        current_node = current_node -> next;
    }

    current_node -> next = CreateRoot(value);
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
void InsertNode(node **root, int value)
{
    node *new_root = CreateRoot(value);
    new_root -> next = *root;
    *root = new_root;
}
```
The advantage of Head Insert is that inserting a new node is always constant time complexity $O(1)$ 

### Searching
A linked list cannot be searched with Binary Search or any other search algorithm other than Linear Search. There's no pointer to an arbitrary position of the list. It must be searched from the beggining to the end

1. Iterate through all the nodes
2. Check if the value being searched for is in the current node
    - If it isn't, set the current node as the next one
3. If reaches a nodes that equals to `NULL`, value isn't in the list.


```c
bool SearchValue(node *root, int value)
{
    node *current_node = root;
    while (current_node != NULL)
    {
        if (current_node -> data == value)
        {
            return true;
        }
        else{
            current_node = current_node -> next;
        }
    }
    return false;
}
```

### Deleting List
Deleting a whole linked list must be done by `free`ing node by node. If we just free the root node, we will be left with a huge memory leak from the orphan nodes.  
A linked list can be `free`d easily through recursion

1. Start at the first node
    - While it isn't null, recall function passing the next node as argument
        - Free current node
        - Set it to `NULL`

```c
void DeleteList(node *root)
{
    node *current_node = root;

    while (current_node != NULL)
    {
        DeleteList(current_node -> next);
        free(current_node);
        current_node  = NULL;
    }
}
```
