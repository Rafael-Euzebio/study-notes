# Encapsulation
Encapsulation is a [[Univesp Object Oriented Programming]] concept which consists of hiding the implementations of [[Univesp Methods]] inside an object  
The methods of an object can, essentially, be hid from the end user and even from the programmer, as long as it does what it is expected to do

## Example
```py
mylist = [0, 80, 20, 40, 80]
print(mylist)

mylist.sort()

print(mylist)
```
```
[0, 80, 20, 10, 50]
[0, 10, 20, 50, 80]
```
In the above codeblock a `.sort()` method sorts a list object. Unless we decide to dive in in Python's source code, we don't know how `.sort()` is implemented, what kind of sorting algorithms it uses, etc. All we know is that it sorts a list

Even if the list contains a data type that might be tricky to sort, like `strings`

```py
mylist = ["0", "80", "20", "40", "80"]
```
```
['0', '80', '20', '40', '80']
['0', '20', '40', '80', '80']
```
