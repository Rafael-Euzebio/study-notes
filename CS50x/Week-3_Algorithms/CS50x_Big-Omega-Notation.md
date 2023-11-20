# Big Ω (Omega) Notation
Big Ω (Omega) Notation is [Asymptotic Notation](./CS50x_Asymptotic-Notation.md) used to describe an algorithm's complexity and efficiency in the best case scenario (called *lower bound*).

## Example
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
The `to_search` number can be anywhere in the `n` array. In the best case scenario, it will be at the first position, and the array will only have to be iterated once.
This can be expressed as:  
$Ω(1)$
