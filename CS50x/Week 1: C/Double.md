# Double
Double is a [[Primitive Data Types|Primitive Data Type]] used to store decimal numbers with *floating points*.

- Size (bytes): 8
- Format specifier: %lf

## Precision
Even though its purpose is similar to the *float* data type, double stores numbers with **double precision**.

Its precision is up to 15 digits (**But varies depending on the system's architecture**). If more precision is needed, [[Long Double]] can be used.
The disadvantage is that it occupies twice the memory as float.

## Example
```C
int main(void){
    int a = 1; 
    int b = 3;
    int c = a/b;
    
    printf("%.20lf", c);
}
```

**Output**
> 0.33333333333333331483
