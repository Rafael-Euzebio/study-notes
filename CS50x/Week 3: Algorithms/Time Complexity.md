# Time Complexity
Time Complexity specifies how long it will take to execute a algorithm as the input size grows. It **does not** describes actual runtime, since actual runtime varies due to `hardware` and `Operational System`.

## Function of its input size
Time Complexity is said to be a ***function of its input size***. That means it describes how long it will take to execute the algorithm as the input size grows?

The following code block receives an `integer` as input and then computes a sum based on the input.
If input is 4, it will add 1 + 2 + 3 + 4 = 10.

```c
int calculateSum(int input)
{
    int sum = 0;

    for (int i = 0; i <= input; i++)
    {
      sum += i;
    }

    return sum;
}
```

The above code can be divided in 3 statements:
1. variable `sum` declaration
2. `for loop`
3. `return`

The `for loop` is executed according to user input, if the input is 4 then it will run 4 times.

That means the amount of operations is `input + 2` times, and input can be any number. So it is a ***function of its input size***

## Representation

| Representation |          Type           |
|--------------- | ------------------------|
| (1)           | [[Constant Time]]        |
| (n)           | [[Linear Time]]          |
| (n log n)     | [[Logarithmic Time]]     |
| (n^2)         | [[Quadratic Time]]       |
| (2^n)         | [[Exponential Time]]     |
| (n!)          | [[Factorial Time]]       |
