# Selection Sort
Selection Sort is a [[Sorting Algorithms|Sorting Algorithm]] that takes the smallest element in an array and places it at the beginning of the array.

## Pseudocode
```
Loop through the array until the second to last item
    define the Nth step of the loop as the minimum index
    Loop through the array starting from the minimum index
        If array[i] is less than array[minimum_index]
            swap them
```

## C Code

```c
#include <stdio.h>

void SelectionSort(int data[], int size);

int main(void)
{
    int data[] = {20, 12, 10, 15, 2};
    int size = sizeof(data) / sizeof(data[0]);
    SelectionSort(data, size);
}

void SelectionSort(int data[], int size)
{
    for (int step = 0; step < size - 1; step++)
    {
        int min_index = step;

        for (int i = step + 1; i < size; i++)
        {
            if (data[i] < data[min_index])
            {
                min_index = i;
            }
        }
        int temp = data[step];
        data[step] = data[min_index];
        data[min_index] = temp;                
    }                                          

    for (int i = 0; i < size; i++)
    {
        printf("%i\n", data[i]);
    }
}
```

## Performance
Selection Sort *Time Complexity* is [[Quadratic Time]] or $O(n^2)$, which makes it inneficient on large lists.
