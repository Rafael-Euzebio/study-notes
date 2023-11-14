# Logarithmic Time
Logarithmic Time Complexity means the [Time Complexity](./CS50x_Time-Complexity.md) of an algorithm grows logarithmically according to input size.  
[Logarithm](./CS50x_Logarithm.md) is the opposite of exponentation, which is characterized by repeteadly multiplications, hence a logarithm time complexity is characterized by multiple divisions of the input $n$.  
That means even if the input $n$ doubles up, only one more operation will be performed.  
This is usually represented as:  
$O(log$  $n)$

## Base-2
In computer science Logarithmic Time Complexity is specified as $O(log{_2}n)$ but simplified to $O(log$ $n)$.  
The reason for that is that base-2 comes up frequently when designing algorithms:  
- Dividing arrays in half, with sorting or search operations  
- When doing bit operations – for instance, writing a number in binary uses about log2(n) bits
