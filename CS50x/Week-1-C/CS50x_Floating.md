# Float
Float is a [Primitive Data Types](./CS50x_Primitive-Data-Types.md) used to store decimal numbers and exponential numbers with *floating points*.

- Size (bytes): 4
- Format Specifier: %f

## Precision
Float's precision is up to 6 digits (**but varies depending on the system's architecture**), if more precision is needed, [Double](./CS50x_Double.md) can be used.

## Example
A float variable is declared as below:

```C
int main(void){
    float a = 1;
    float b = 3;
    float c = a/b;

    printf("%.20f", c);
}
```

**Output**
> 0.33333334326744079590



