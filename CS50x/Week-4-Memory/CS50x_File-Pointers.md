# File Pointers
File pointers are [Pointer](./CS50x_Pointer.md) to a *structure* of a stored file. Said structure contains all the information neecessary to work with that file through functions.


## Functions
All funtions below comes from the `stdio.h` library. These are not all functions related to file manipulation, just the most common ones.

| Function | Description     |
| -------- | --------------- |
| `fopen()`| Opens a file    |
| `fclose()`| Closes a file    |
| `fgetc()`| Gets a `char` from a file|
| `fputc()`| Inserts a `char` into a file|
| `fread()`| Reads a given amount of bytes from a file|
| `fwrite()`| Writes a given amount of bytes into a file|
| `fseek()`| Changes the current position where information can be written/be read into/from the file|
| `ftell()`| Returns the current position where information can be written/be read into/from the file|
| `fgets()`| Reads a line from the file|

- fopen
- fclose
- fgetc
- fputc
- fread
- fwrite

### fopen
```c
FILE *fopen(const char *filename, const char *mode)

FILE *file = fopen("file.csv", "a");
```
`fopen()`, opens a file. It takes two arguments:   
1. filename
2. mode

Each mode interacts with the file in a different way. 

#### Modes

|File access mode string 	| Meaning 	    | Explanation 	                | Action if file already exists 	| Action if file does not exist |
|---------------------------|---------------|-------------------------------|-----------------------------------|-------------------------------|
|"r"                        |read 	        |Open a file for reading 	    |read from start             	    |failure to open                 
|"w"                        |write 	        |Create a file for writing 	    | destroy contents             	    |create new
|"a"                        |append 	    |    Append to a file 	        |    write to end 	                |create new
|"r+"                       |read extended 	|Open a file for read/write 	|    read from start             	|error
|"w+"                       |write extended |	Create a file for read/write|    destroy contents             	|create new
|"a+"                       |append extended| Open a file for read/write 	|    write to end 	                |create new

It returns a *File pointer*.

### fclose
```c
int fclose(FILE * stream)

fclose(file);
```
`fclose` closes the file opened with `fopen`. It takes as arguments:  
- *file pointer* 

If succesful to so, zero is returned

### fgetc
```c
int fgetc(FILE *stream);

FILE *file = fopen("test.txt", "r");

char ch;
while ((ch = fgetc(file)) != EOF)
{
    printf("%c", c);
}
return 0;
```
*EOF* = *End of File*.

`fgetc` gets the next character (or the very first, if it hasn't executed before) from a file.  
- *file pointer*

It returns an `int` (which can be stored in a char variable) if succesful. 

### fputc
```c
int fputc( int ch, FILE *stream );
	
FILE *file = fopen("teste.txt", "w");
fputc('A', file);
```

`fputc` writes or appends (depending if the file pointer operation is `w` or `a`) a character to a file.  
1. `char`
2. *file pointer*

It returns the written character if succesful

### fread
```c
fread( void *buffer, size_t size, size_t count, FILE *stream );

char s[5];
FILE *file = fopen("test.txt", "r");
fread(s, sizeof(char), 5, file);
printf("%s", s);
```

fread reads a given amount of objects in a file.
In the above codeblock the objects are `char`s, 

1. *pointer* to a variable
2. object size
3. number of objects
4. *file pointer*

`fread` is reading `5` chars of size of a `char` (1 byte) and storing it in the array `s`  
Calling fread again with the same file pointer will read from the last position

### fwrite
```c
fwrite(void *buffer, size_t size, size_t count, FILE *stream);
char s[] = "Some text";
FILE *file = fopen("test.txt", "a");

fwrite(s, sizeof(char), strlen(s), file);
```

fwrite works the same way as `fread`, but instead of getting objects from the file and storing it in a variable, it does the opposite.

### fseek
```c
fseek(FILE *stream, long int offset, int whence)
```
fseek changes the file position of a file stream to the given offset  

`FILE *stream` = File pointer  
`long int offset` = number of bytes to offset from whence  
`whence` = The position to where offset is added, it can be 3 different values:
    - `SEEK_SET`: Beggining of the file
    - `SEEK_CUR`: Current position
    - `SEEK_END`: End of the file

### ftell
```c
long int ftell(FILE *stream)
```
Returns the current file position of a file stream

`FILE *stream` = File pointer

### fgets
```c
fgets(char *str, int n, , FILE *stream)
```

fgets reads a line from the file, and stores it in a buffer. It stops when the size `n` is reached or it reaches a new line

`*str` = Buffer to store the string   
`n` = Maximum amount of characters to be read. Usually the size of `*str`  
`FILE *stream` = File pointer

