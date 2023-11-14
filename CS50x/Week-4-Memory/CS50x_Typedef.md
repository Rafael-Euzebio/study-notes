# Typedef
Typedef is a keyword used to create [User Defined Data Types](./CS50x_User-Defined-Data-Types.md), usually an alias to an existing data type or [Structures](../Week-3-Algorithms/CS50x_Structures.md)

## Example
```c
typedef *char string
```

This creates a type `string`, which is a pointer to the first char of an array of chars.

```c
/// These are the same
char *array = "Hello";
string s = "World";
```

## Structure
Typedef allows us to give an alias to [Structures](../Week-3-Algorithms/CS50x_Structures.md)

```c
typedef struct person
{
    char name[20];
    int age;
} 
person;
```
 or
```c

typedef struct
{
    char name[20];
    int age;
}
person;
```

```c
person person1 = {"David", 20};
```

#### Important: Typedef scope
In the following code the word `person` is a *struct identifier*.
```c
struct person
{
    char name[20];
    int age;
};
```

While in the following code the word `person` at the end is an *alias* for the structure.
```c
typedef struct person
{
    char name[20];
    int age;
} 
person;
```
These two names are *different things* and maintened in *different scopes*, for that reason they do **not** colide.  
But `typedef` scope is the same as `variables`, so a variable cannot be assigned with the name of `person`.

s
