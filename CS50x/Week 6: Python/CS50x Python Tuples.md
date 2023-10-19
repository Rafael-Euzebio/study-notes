# Python Tuples
Tuples are a [[CS50x Python Sequences Types]] used to store values, similar to a list, but the values are immutable, hence, cannot be changed

## Example

```py
person = ("John", 23)
name, age = person
print(name, age)
```
`John, 23`

The above codeblock creates a tuple `person`, with two values.   
The values do not have names to be refereced, the items in a tuple must be acessed as a list would, with `[index]`  
But the values can also be assigned to variales, declared in the same order that the values appear  

```py
presidents = [
        ("George Washignton", 1789),
        ("John Adams", 1797),
        ("Thomas Jefferson", 1801),
        ("James Madison", 1809),
]

for president, year, in presidents:
    print("In {1}, {0} took office".format(president, year))
```

```
In 1789, George Washignton took office
In 1797, John Adams took office
In 1801, Thomas Jefferson took office
In 1809, James Madison took office
```

The above codeblock creates a list of tuples, each tuple in the list contains the name of a president and the name they got in office  
the `for loop` attributes a variable to each item on each tuple (`president` for index `0` and `year` for index `1`) and then prints it, plugging the values in the `{index}`

In other words:
```py
for i in range(len(presidents)):
    print("In {1}, {0} took office".format(presidents[i][0], presidents[i][1]))
```


