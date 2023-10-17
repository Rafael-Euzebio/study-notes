# Condition-Controlled Loops
A condition-controlled loop is a loop statement that is only if a condition evaluates as *true*

Its used when we don't know how many times that loop will have to be executed, especially because of external factors like *user input*

## Types
There are 2 types of condition-controlled loops, *while* and *do while*

### While
A while loop will check for the condition first and then execute the loop if that condition evaluates as true.

```C
#include <stdio.h>
int main(void){
    int i = 1;
    while(i <= 10){
        printf("%d\n", i);
        i++;
    }
}
```
> The above codeblock will print `i` 10 times, from 1 to 10;

**Even though similar to a count-controlled loop, the difference is that the `while` loop *doesn't expect a count*, it can be any other condition.**

```C
#include <stdio.h>
#include <cs50.h>

int main(void){
    int positive_number; 
    do{
        positive_number = get_int("Insert a positive number"); 
    } while(positive_number < 0);

    printf("%d\n", positive_number);
}
```
**Output**
> The above codeblock will keep reprompting the user to enter a positive number if they insert a number lower than 0.
> Then it will print the number.

That would *not* be achievable by a [[#While]] loop since it **checks the condition first** before iterating the loop
**Do While do a first iteration before checking the condition**
