# Heap
The heap is a reserverd part of the system's memory that the programmer can make use of as they see as necessary.


# Heap Memory
The heap is located on lower addresses, below the *stack* but above the *bss*, as it is used the heap grows upwards, towards the *stack*.
The programmer is completely responsible for managing the memory in the heap, through [Dynamic Memory Allocation](./CS50x_Dynamic-Memory-Allocation.md), allocating and freeing memory as they see necessary.

```
================    Highest Address (e.g. 0xFFFF)
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

Different than the heap, memory allocated in the heap can be `free`d at any time in any order.

