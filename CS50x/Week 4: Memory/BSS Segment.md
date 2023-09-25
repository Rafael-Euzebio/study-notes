# BSS Segment
The BSS (Block Starting Symvol) segment is a reserved part of an executable file or system's memory to store unintialized [[Static Variable]]

## Example
The following codeblock creates a simple c code with no variables
```c
#include <stdio.h>

int main(void)
{
    return 0;
}
```
compiling it with   
`gcc -ggdb -c (filename).c`  
generates a (filename).o file, which can be analyzed with the size command  
`size (filename).o`  

```
   text    data     bss     dec     hex filename
    103       0       0     103      6b memory.o
```

if we add a single unintialized static variable
```c
static int i;
```
the output is
```
   text    data     bss     dec     hex filename
    103       0       4     107      6b memory.o
```

We see the bss segment has 4 bytes stored in it, the exact size of an int

## BSS Memory
The BSS segment is located in the lower addresses of the memory, below the *heap*
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
`
