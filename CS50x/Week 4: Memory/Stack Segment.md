# Memory Stack
The Memory Stack is a reserved part of the system's memory used to allocate memory for [[Local Variable]] and functions.  
The Memory Stack is an implementation in memory of a [[Stack]] *Abstract Data Type*

## Call Stack
The Call Stack is a data structure responsible to store the information of which subroutines (functions) haven't yet exited, and are still active in the stack.

- There can be multiple instances of a single [[Local Variable]] present in the call stack   
    - This is why recursion works

### Stack Pointer
The Stack Pointer stores the memory address of the function at the top of the stack. When a function is called it is added to the stack at the next memory address and the stack pointer is updated. When a function exits it is removed from the stack and the stack pointer is updated on the opposite direction

## Stack Memory
The Stack memory is located on higher addresses, above all other segments. The stack grows downwards as it's space is used.
The programmer is not responsible for managing the stack memory, when a function exits its block in the stack is freed automatically and when it is called a block is added at the top of the stack. That's called [[Automatic Memory Allocation]]  
One must be careful to not use all memory avaliable for the stack though, especially when dealing with *loops* and *recursive functions*, if the program never exits their scope it will result in a [[Stack Overflow]]

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
