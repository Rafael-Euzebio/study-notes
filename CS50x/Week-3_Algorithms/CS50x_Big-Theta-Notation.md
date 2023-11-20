# Big Θ (Theta) Notation
Big Θ (Theta) Notation is a mathematical notation used to describe an algorithm's complexity and efficiency when the upper bound ([Big O Notation](./CS50x_Big-O-Notation.md)) and the lower bound [Big Omega Notation](./CS50x_Big-Omega-Notation.md) is the same.

Big O Notation and Big Ω Notation describe, respectively, worst case scenario and best case scenario.  
But for some algorithms, these are the same. When that's the case, we can give it a Big Θ. 

## Examples
Take the following linear search algorithm as example:
```c
bool SearchNumber(int n[10], int to_search)
{
    for (int i = 0; i < 10; i++)
    {
        if(n[i] == to_search)
        {
            return true;
        } 
    }
    return false;
}
```
It has a Big O Notation of $O(n)$ and a Big Omega Notation of $Ω(1)$.  
What about a Big Theta? It doesn't has one. Since the amount of operations isn't the same on lower bound and upper bound, it's not possible to attribute a Big Theta.

But one can be attributed to the following algorithm:

```c
void Print(int n[10])
{
    for (int i = 0; i < 10; i++)
    {
        printf("%i", n[i]);
    }
}
```
This algorithm prints every item within the `n` array, so the upper bound and lower bound are the same, $O(n)$ and $Ω(1)$.  
So we can say this algorithm has a Big Theta of $Θ(n)$
