# Big O notation
Big O notation is [[CS50x Asymptotic Notation]] used to describe an algorithm's complexity and efficiency in the worst case scenario (called *upper bound*).

## Example
Taking the following linear-search algorithm as example:
```c
bool function(int n, int to_search) //assume n as an array of size 10 and to_search as a number to be searched in the array
{
    for(int i = 0; i < 10; i++)
    {
        if(n[i] == to_search)
        {
            return true;
        } 
    }
    return false;
}
```
The `to_search` number can be anywhere in the `n` array. In the worst case scenario, it will be at the last position, or not even be in the array, and the array will have to be iterated fully until the function returns.
This can be expressed as:  
$O(n)$  
