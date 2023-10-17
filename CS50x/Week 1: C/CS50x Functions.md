# Functions
A function is a *named* sequence of code that perform a task.
Since they are named functions can be *called* in another part of the code. 

In C functions are Derived Data Types, and its type is specified before its name when declared

## Arguments
A function may or may not ask for ask for a *argument*, that is, a value to work with. This value is passed to the function inside the *()* 

## Declaring or importing functions
Functions can either be declared and built or imported.
In every C program the user will declare at least one function, called `main()`, declared as below.
```C
int main(void){
	#Code
}
```

### Declaring functions
More functions can be declared, and then called from inside the `main()`
```C
void myFunction(){
	printf("Function executed");
}
int main(void){
	myFunction();
}
```
**Output**
> "I just got executed"

### Importing functions
Functions can be imported from [[CS50x Libraries]], these are collections of functions that can be used by other developers.

Example, the `printf()` function comes from a library called `stdio.h` and that library must be imported before `printf` is used. See below:
```C
#include <stdio.h>

int main(void){	
	printf("Test");
}
```
