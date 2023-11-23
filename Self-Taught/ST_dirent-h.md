# dirent.h
`dirent.h` is a library for retrieving information about files and directories, written in C

```c
#include <dirent.h>
```

## Types
- `DIR`
    - Represents a directory stream

- `ino_t`
    - Integer representing a serial number

## Structures
```c
struct dirent {
    ino_t d_ino; // File serial number
    char d_name[256]; // Filename
}
```


## Functions

### alphasort
```c
int alphasort(const struct dirent ** (d1), const struct dirent** (d2))
```

- Sorts by alphabetical order, comparing `d1` and `d2`
    - Returns an `int`, greater than, equal to or less than `0`, depending if `d1` comes first than `d2` in alphabetical order


### closedir
```c
int closedir(DIR *)
```
- Closes a directory stream
    - Returns an `int` `0` on success and `-1` on error

### dirfd
```c
int dirfd(DIR *)
```
- Returns the file descriptor associated with the directory stream
    - Returns `-1` on error

### fdopendir
```c
DIR *fdopendir(int)
```
- Opens a directory stream corresponding to the file descriptor given to the function
    - Returns a pointer to the DIR object


### opendir
```c
DIR *opendir(const char *)
```
- Opens a directory stream corresponding to the name given to the function
    - Returns a pointer to the DIR object

### readdir
```c
struct dirent *readdir(DIR *)
```
- Returns a pointer to a structure [dirent](#Structures), corresponding to the DIR pointer given to the function

### rewinddir
```c
void rewinddir(DIR *)
```
- Repositions the directory stream to the beggining

### scandir
```c
int scandir(const char *dirp, struct dirent ***namelist, int (*filter)(const struct dirent *), int(*compar)(const struct dirent **) )
```
- Scans the directory `dirp`
    - Applies `filter` on each file
        - `filter` is a function that receives the entry string for some kind of comparison.
            - Only the strings that return nonzero from the function pass the filter
            - If no filter is desired, set it no `NULL`
    - Sorts the entries with `compar`
        - `compar` can be two functions, `alphasort` or `versionsort`
    - Stores the entries in the array `namelist`

### seekdir
```c
void seekdir(DIR *dirp, long loc)
```
- Sets the location in the directory stream for the next `readdir` call. `loc` should be a value returned by `telldir()`

### telldir
```c
long telldir(DIR *)
```

- Returns the current location in the directory stream


            

