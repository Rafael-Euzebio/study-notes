# Structures
A structure is a collection of multiple variables under a common name. They are used to group together correlated information.  
With structures you can treat multiple related variables as a single one, and reference each one of the variables when necessary.  

## Declaring Structs
Structs are declared with the keyword `struct`.

```c
struct person
{
    char name[20];
    int age;
};
```
Each variable inside the structure is a *member* of that structure.  
The code above defines a `struct`ure `person` that contains a `char`acter `array` for *name* and a `int`eger variable for *age*.  
The structure is now considered a data type, and variables of that data type can be created as follows:  

```c
struct person person1 = {"David", 20};
```

### Typedef
A cleaner way is to attribute an `alias` to that structure when defining it by using [Typedef](../Week-4_Memory/CS50x_Typedef.md).  

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

Then the keyword `struct` doesn't has to be used when creating variables of said structure.  
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

## Acessing data
After a variable of the `struct` type been declared, its data can be read (and written) through the `.` (dot) operator and the corresponding `tag` of the data  
```c
person person1 = {"David", 20};

printf("%s, %i", person1.name, person1.age);
```