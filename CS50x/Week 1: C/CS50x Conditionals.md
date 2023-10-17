# Conditionals
Conditionals are [[CS50x Statements]] for handling decisions. Conditionals perform different actions depending if a [[CS50x Boolean]] condition is *true* or *false*.

## Example
```C
#include <cs50.h>
int main(void){
	int x = get_int("What's x? ");
	int y = get_int("What's y? ");

	if (x < y){
		printf("x is less than y");	
	}
	else if(x > y){
		printf("x is greater than y");	
	}
	else{
		printf("x and y are equal");	
	}
}
```
The above code block asks the user to define 2 values, *x* and *y*, and then compares these values, using the `if else` statement, giving a different output depending if *x* is less, greater or equal to *y*.

**Important**: There's no need to use `else if` in the last statement, since this is the only possible result and that would only add additional useless operations to the computer. `else` must be used instead.