# Memory Management
Memory Management is the proccess of allocating and deallocating memory performed by a computer.

## Methods
The different methods of allocating and deallocating memory define
- Where in the memory something is written
- When it is safe to read the contents of a [[Memory Address]],
- When the contents and location are no longer safe to access

Those methods are: 
[[Automatic Memory Allocation]]
[[Static Memory Allocation]]
[[Dynamic Memory Allocation]]

## [[Memory Safety]]
While reading from a memory address might not be safe, certain languages do not stop the programmer from doing that, like *C* and *C++*

## Memory Illustration
This is a simple illustration with descriptions of each segments of memory and what kind of allocation is done with them.

```
===============     Highest Address (e.g. 0xFFFF)
|              |
|    STACK     |
|   automatic  |
|    memory    |
|--------------|  <- Stack Pointer
|              |
-  free space  -
|              |
|--------------|  <- Heap Pointer
|              |
|     HEAP     |
|dynamic memory|
|--------------|  
|              |
|     BSS      |
| unitialized  |
|    static    |
|  variables   |
|--------------|  
|              |
|     DATA     |
| initialized  |
|    static    |
|  variables   |
===============     Lowest Address  (e.g. 0x0000)
```
