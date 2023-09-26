# Linked Lists
A linked list is a data structure of a linear collection of elements. The elements are not stored sequentially in memory, like and *array*, instead, each element points to the address of the next one.

## Structure
A linked list is made of *nodes*, each node has a *data* and a *reference* field  

`data` = the value stored in that node
`reference` =  the address of the next node

## Use
Lists are a simple data structure that can be used to implement many *Abstract Data Types*, like [[Stack]] and [[Queue]]


## Example
Example of a linked list which inserts elements like a *stack*
```c
#include <stdio.h>
#include <stdlib.h>

// Defining node struct
typedef struct node
{
    int number;
    struct node *next;
}node;

int main(int argc, char *argv[])
{
    //Initializing a pointer list to a node
    node *list = NULL;

    // Looping through argv values
    for (int i = 1; i < argc; i++)
    {
        //Converting arguments to int
        int number = atoi(argv[i]);

        // Creating a pointer n to a node;
        node *n = malloc(sizeof(node));

        if (n == NULL)
        {
            return 1;
        }

        // Assigning values to node n 
        n -> number = number;
        n -> next = NULL;

        // Linking new node to the last added node (null if it's first iteration)
        n -> next = list;

        // list pointer points to the new node
        list = n;
    }

    /// Iterating through list and printing values
    node *ptr = list;

    while (ptr != NULL)
    {
        printf("%i\n", ptr -> number);
        ptr = ptr -> next;
    }


    /// Iterating through list and freeing pointers
    ptr = list;

    while (ptr != NULL)
    {
        node *next = ptr -> next;
        free(ptr);
        ptr = next;
    }

}
```

## Pros and Cons
A linked list can have values added to it without having to worry about enough memory being allocated in advance, unlike arrays, which must be reallocated to store more values than it size allows.

However, a linked list can only be searched through **linear search**, since it's not possible to access the elements in the middle of the list.
