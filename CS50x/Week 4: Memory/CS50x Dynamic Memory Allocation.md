# Dynamic Memory Allocation
Dynamic memory allocation is a [[CS50x Memory Management]] process, which allows the programmer to allocate memory dynamically as they consider necessary. The programmer is also responsible for *freeing* that memory

## Memory Allocation
Dynamically allocated memory comes from the [[CS50x Heap]] at [[CS50x Runtime]], where the programmer is responsible for managing the used memory through the use of *functions*.

### Functions
All functions below comes from the `stdlib.h` library  
- malloc          
- calloc          
- realloc         
- free            

#### malloc
```c
void* malloc(size_t size)

int *p = malloc(sizeof(int));
```
`malloc` allocates memory in the heap. It takes as argument the amount of bytes the programmer wishes to allocate, and returns a pointer to that memory address.  

#### calloc
```c
void* calloc(size_t num, size_t size)
```
`calloc` allocates memory for an array. It takes two arguments: *The size of the array (number of elements)* and *amount of bytes each element contains*.  
Upon the creation of the array, all elements are initialized to zero.  


#### realloc
```c
void* realloc(void *ptr, size_t new_size)
```
`realloc` reallocates a given memory. It takes two arguments, a pointer to the memory address that must be reallocated, and the size of the new allocated space in memory.  
`realloc` tries to expand the given memory address if possible (aka, if there isn't any allocated content after it), if not it executes the following steps:
1. Allocate the memory specified in `new_size`
2. Copy the values from `*ptr` to the new memory address
3. Free the old memory address
4. Returns the new pointer

#### free
```c
free(void *ptr)
```
accepts a pointer, which points to a memory address allocated by the functions above. It frees that memory address, ending the lifetime of the pointer variable.  
*It is considered a good practice to assign NULL to the pointer variable to prevent the programmer from trying to access it again or a **double free***

## Lifetime and Scope
The lifetime of an allocated pointer variable is up to the moment it is `free`d. After than it is not safe to read or write that memory location and it's considered a good practice to set that pointer to `NULL` after `free`ing it.
Its scope is the block or function that pointer is declared.


