# Binary Search
Binary Search is a [[Search Algorithms|Search Algorithm]] for searching an item within a **sorted** list.  
It consists of checking the middle item of the list, and if that's not the desired item the half which the desired item cannot be is eliminated, and then repeating the process.


## Pseudocode
1. The array where the search is performed is defined: 
    `3, 4, 5, 6, , 7, 8, 9`
2. The number being searched for is defined:
    `7`
3. Two pointers are set, `low and high`, at the lowest and highest positions of the array
4. Find the middle of the array, defined as `mid` through `array[low + (high - low) / 2]`
> This could also be done with `low + high / 2` but the first method avoid overflows
5. if `x` is equal to `array[mid]` then `return` its position 
6. if `x` is greater than `array[mid]`, then eliminate the lower half and repeat step 3. This is done by setting `low` to `low = mid + 1`
7. if x is is lower than `array[mid]`, then eliminate the greater half and repeat step 3. This is done by setting `high` to `high = mid - 1`

## Example

```c
#include <stdio.h>

int BinarySearch(int array[], int x, int low, int high);

int main(void)
{
    //Sorted Array
    int array[] = {3, 4, 5, 6, 7, 8, 9};

    //Getting array length
    int n = sizeof(array) / sizeof(array[0]);

    //x = desired item
    int x = 7;
    int result  = BinarySearch(array, x, 0, n - 1);

    if (result == -1)
    {
        printf("Not found\n");
    }
    else
    {
        printf("Element is found at index %d\n", result);
    }
    return 0;
}

int BinarySearch(int array[], int x, int low, int high)
{
    while (low <= high)
    {
        int mid = low + (high - low) / 2;

        if (array[mid] == x)
        {
            return mid;
        }

        if (array[mid] <= x)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }
    return -1;
}

```
## Implications
For binary search work correctly the data structure being searched must be sorted. This is done through [[Sorting Algorithms]]. This creates a trade off where to use a faster search algorithm an extra step must be taken before performing the search.

## Time Complexity
Its time complexity is [[Logarithmic Time]]
