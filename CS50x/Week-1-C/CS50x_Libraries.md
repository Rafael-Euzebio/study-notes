# Libraries
A library is a collection of code which includes [Functions](../Week-1-C/CS50x_Functions.md) to be used by other programmers.

Libraries prevent programmers from having to rewrite functions used often in every single program and minimize the risks of insecure code being written, since the security standards are applied in the library.

## Example
Libraries must be imported before their functions are executed, like the following example in C:

```C
#include <stdio.h>
int main(void){
	printf("This function comes from stdio.h library")
}
```