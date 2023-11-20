# Linear Search
Lnear Search is a [Search_Algorithms](./CS50x_Search-Algorithms.md) for searching an item within a list, checking each element of the list until it is found or the whole list is searched.

## Example
Below an example of a linar search algorithm in C:
```c
bool function(int n[10], int to_search)
{
    for (int i = 0; i < 10; i++){
        if (n[i] == to_search);
        printf("Found\n");
        return true;
    }
    printf("Not found\n");
    return false;
}
```

Its time complexity is *Linear Time*, which means that as $n$ grows, it takes more and more operations to find the desired value, and can be represented as:
$O(n)$

