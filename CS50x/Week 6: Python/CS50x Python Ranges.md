# Python Ranges
A range in a python is a sequence of numbers that cannot be changed, and a [[CS50x Python Sequences Types]]

## Example
A range is declared as follows:    
`range(10)`

The values of the range can be printed with:
`print(list(range(10)))`  
`[0, 1 , 2, 3, 4, 5, 6, 7, 8, 9]`

A `start` value can be added:    
`print(list(range(5, 10)))`  
`[5, 6, 7, 8, 9]`

Also a `step` value:  
`print(list(range(0, 10, 2)))`  
`[0, 2, 4, 6, 8]`

Or be used in loops

```py
for i in range(10)
    print(i)
```
```
0
1
2
3
4
5
6
7
8
9
```


***A range does not returns all values at once. Instead it only stores the `start` `stop` and `step` value, and then do arithmetics with them. For that reason a range uses less memory than `lists` or `tuples`***
