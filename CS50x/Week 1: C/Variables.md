# Variables
Variables are a container which stores a certain amount of information, which is refered as value. 

## Declaring a variable
Variables can contain different [[C Data Types]] , and some languages require you to specify the data type intended to be used in that variable.

That's how a integer variable is declared in C:
```C 
int main(void){
    int value = 1; 
}
```

Variables with different [[C Data Types]] bellow:

```C
int main(void){
    char letter = 'A';
    bool not_true = false;
}
```

## Declaring Variables
Variables can be referenced after being declared, that way you can use the stored value with Operators or Functions, Conditionals, Loops etc...

That's how we sum two values stored in different variables in C:
```C
int main(void){
    int first_value = 1;
    int second_value = 2;
    int result = first_value + second_value;

    printf("The result is: %d", result);
}
```
In the above code block `%d` is necessary to display a variable's value. 
