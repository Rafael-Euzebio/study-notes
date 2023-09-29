# Doubly-Linked Lists
A singly-linked list is a [[Linked Lists]] data structure, a linear collection of elements. The elements are not stored sequentially in memory, like and *array*, instead, each element points to the address of the next one.

## Structure 
A doubly-linked lists is made of *nodes*, eachnode has a *data*, a *next* and a *prev* field:  
- `data` = the value stored in that node 
- `next` =  the address of the next node 
- `prev` =  the address of the previous node

## Example

```c
typedef struct node
{
    int data;
    struct node *prev;
    struct node *next;
} node;
```

### Creating a Linked List
To create a linked list we first need to create our `root` node.

1. Allocate memory for that node
2. Set its `next` field to `NULL`
3. Set it `prev` field to `NULL`
4. Fill it's `data` field
5. Return it's address

```c
int main()
{
    node *root = CreateRoot();
}

node *CreateRoot(int value)
{
    node *root = malloc(sizeof(node));
    root -> next = NULL;
    root -> prev = NULL;
    root -> data  = value;

    return root;
}
```

### Inserting Nodes
#### Tail Insert
Tail Insert refers to a linked list which new nodes and values are inserted at the very end, one after the other.  
The steps to do that with doubly-linked lists are:

1. Iterate through all nodes, starting at the root.
2. Check if current node points to a `NULL` value
    - If current node points to another node, set current node to `next` and repeat
3. Create a new node
    - We can use the earlier function `CreateRoot()` to do that. Each node is a "root" to the next one
4. Set the `next` field of the current node to new node
5. Set the `prev` field of the new node to current node

```c
void InsertNode(node *root, int data)
{
    node *current_node = root;

    while (current_node -> next != NULL)
    {
        current_node = current_node -> next;
    }

    node *new_node = CreateRoot(data);
    current_node -> next = new_node;
    new_node -> prev = current_node;
}
```

The disadvange of Tail Insert is that adding new nodes is always linear time complexity $O(n)$

#### Head Insert
Head Insert refers to a linked list which new nodes are inserted at the begginging at the list. New nodes coming before old ones.  
To do that it is necessary to keep changing the root pointer to the new node after every insertion.  

1. Create a new node
2. Fill the `data` field of the new node
3. Change `next` field in new node to point to `root`
4. Change `prev` field in root to new node
5. Change `root` pointer to point to new node (new root)
```c
void InsertNode(node **root, int data)
{
    node *current_root = *root;
    node *new_root = CreateRoot(data);
    
    new_root -> next = *root;
    current_root -> prev = new_root;
    *root = new_root;
}
```
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

### Deleting Single Node
Deleting a single node in a doubly-linked list is fairly easy, compared to *singly-linked lists*. Since we **always have access to the next and previous node**

#### In the middle of the list
1. Iterate through nodes, checking for a `NULL` node
2. If current node has the data we're looking for
3. Set previous node's `next` field as the next node
4. Set next node's `prev` field as the previous node
5. `free` current node and set it to `NULL`
```c
bool DeleteNode(node *root, int data)
{
    node *current_node = root;
    while (current_node != NULL)
    {
        if (current_node -> data == data)
        {
            node *previous_node = current_node -> prev;
            node *next_node = current_node -> next;

            previous_node -> next = next_node;
            next_node -> prev =  previous_node;

            free(current_node);
            current_node = NULL;
            return true;
        }
        current_node = current_node -> next;
    }
    printf("Not found\n");
    return false;
}
```

#### In the edges of the list (First and last node)

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
