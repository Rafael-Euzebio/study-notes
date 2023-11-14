# Static Memory Allocation
Static Memory is a [Memory Management](./CS50x_Memory-Management.md) proccess that reserves memory for a [Static Variable](./CS50x_Static-Variable.md)

## Memory Allocation
Static Memory Allocation happens at [Compile Time](./CS50x_Compile-Time.md), but its more accurate to say that it is handled at compile time.  
This is handled differently by compilers but two options are:  
- Create a [Data Segment](./CS50x_Data-Segment.md) in the final binary, used to store *static variables*
    - This has the disadvantage of increasing the final binary file size, which might be a problem for programs that use a lot of *static variables*
- Inject initialization code that will allocate memory before the program is executed
- The [Data Segment](./CS50x_Data-Segment.md) is only used if the variable is initialized. Otherwise it is stored in the [BSS Segment]
