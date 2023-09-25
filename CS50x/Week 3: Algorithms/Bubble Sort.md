# Bubble Sort
Bubble Sort is a [[Sorting Algorithms|Sorting Algorithm]] that takes larger elements in a array and places it at the end.  
Its called "bubble sort" because the larger elements bubble their way up in the array, like air bubbles in water rising to the surface  

## Pseudocode
```
Loop through the whole array 
    Loop until the second to last element of the array
        If array[i] is greater than array[i + 1]
            swap them
```

## C code
```c
#include <stdio.h>

void BubbleSort(int array[], int size);
void PrintArray(int array[], int size);

int main(void)
{
    int data[] = {20, 12, 10, 15, 2};

    int size = sizeof(data) / sizeof(data[0]);

    printf("Unsorted Array:\n");
    for (int i = 0; i < size; i++)
    {
        printf("%i ", data[i]);
    }

    BubbleSort(data, size);
    PrintArray(data, size);
}

void BubbleSort(int array[], int size)
{
    // Loop array 
    for (int step = 0; step < size - 1; step++)
    {
        // loop until the second to last element
        for (int i = 0; i < size - step - 1; i++)
        {
            //compare elements
            if (array[i] > array[i + 1])
            {
                //swap
                int temp = array[i];
                array[i] = array[i + 1];
                array[i + 1] = temp;
            }
        }
    }
}

void PrintArray(int array[], int size) {
    printf("\nSorted Array\n");
    for (int i = 0; i < size; ++i) {
        printf("%d  ", array[i]);
    }
    printf("\n");
}
```

## Performance
Bubble Sort *Time Complexity* is [[Quadratic Time]], or $O(n^2)$, which makes it inneficient for large lists.
