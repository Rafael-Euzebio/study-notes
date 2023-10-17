# Compile Time
Compile time is the time window a source code is being *compiled* into machine code by a [[CS50x Compiler]]. 

## Memory Allocation
Memory for a program might be allocated at compile time, this is true for [[CS50x Static Memory Allocation]]

## Errors
The term *Compile Time* can be used to refer to the requirements that a program must meet to be compiled succesfully by the compiler.  
A compiler might throw innumerous errors when compiling a program. These errors might be: 
- Incorrect value assignment to a variable (assigning an integer to a char type)
- Incorrect syntax
- Calls to functions that do not exist, or aren't included in the header files
- etc...

When an error is thrown by the compiler that means the source code do not meet the language requirements to be compiled, and must be fixed first.