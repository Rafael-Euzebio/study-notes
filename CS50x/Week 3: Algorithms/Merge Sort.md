# Merge Sort
Merge Sort is a [[Sorting Algorithms|Sorting Algorithm]] that divides its input in half several times, sorts them separately and merges them.  
Its based on the principle of [[Divide and Conquer Algorithm]], usually through the use of [[Recursion]]
## Pseudocode
```
if array is not splitted in single indexes  
    split array recursively defining the right and left portion each time  
    loop through left and right portions and through the original array
        If the left[i] is less than right[j]
            copy left[i] to array[k]
        else
            copy right[j] to array[k]
```

## C code
```c
#include <stdio.h>

void merge_sort(int a[], int length);
void merge_sort_recursion(int a[], int l, int r);
void merge_sorted_arrays(int a[], int l, int m, int r);


int main(void)
{
    int array[] = {9, 4, 8, 1, 7, 0, 3, 2, 5, 6};
    int length = sizeof(array) / sizeof(array[1]);

    merge_sort(array, length);
    
    //print array
    for (int i = 0; i < length; i++)
    {
        printf("%d", array[i]);
        printf("\n");
    }

    return 0;
}

void merge_sort(int a[], int length)
{
    //Call recursion function passing the whole array, the first and the last index as left and right
    merge_sort_recursion(a, 0, length - 1);
}

void merge_sort_recursion(int a[], int l, int r)
{
    // Keep splitting while portions aren't a single index
    if (l < r)
    {
        //define middle index
        int m = l + (r - l) / 2;

        //split array recursively, defining the right portion
        merge_sort_recursion(a, l, m);

        //split array recursively, defining the left portion
        merge_sort_recursion(a, m + 1, r);

        merge_sorted_arrays(a, l, m, r);
    }
}


void merge_sorted_arrays(int a[], int l, int m, int r)
{
    //Getting splitted arays size
    int left_length = m - l + 1;
    int right_length = r - m;

    //Temporary Arrays
    int temp_left[left_length];
    int temp_right[right_length];


    //Copying left portion of the array to the temporary array
    for (int i = 0; i < left_length; i++)
    {
        temp_left[i] = a[l + i];
    }

    //Copying right portion of the array to the temporary array
    for (int i = 0; i < right_length; i++)
    {
        temp_right[i] = a[m + 1 + i];
    }

    int i, j, k;
    //iterating through left and right portions of the array
    for (i = 0, j = 0, k = l; k <= r; k++)
    {
        //copying the smallest value from left or right portion to the original array in each iteration
        if ( (i < left_length) && (j >= right_length || temp_left[i] <= temp_right[j]))
        {
            a[k] = temp_left[i];
            i++;
        }
        else
        {
            a[k] = temp_right[j];
            j++;
        }

    }
}
```

## Time Complexity
Merge Sort *Time Complexity* is *Logarithmic Time*, or $O(n$ $log$ $n)$, which makes it efficient even for large lists.
