# Tries
A trie is a [Tree](./CS50x_Tree.md) [Data Structures](./CS50x_Data-Structures.md) which associates keys and values, with links between nodes defined by a single character from the key.  
It consists of a set of nodes, each having other nodes connected to it and a value, that may or may not be set to something  
The key defines what other nodes will be accessed, by computing them to a index.  

## Example
```
typedef struct TrieNode
{
    struct TrieNode* paths[10];
    char  university[20]; 
} TrieNode;
```

The above structure defines a trie node. It has 10 pointers to other nodes and a `char array` which stores the name of a university.  
The key must be a year, which is when its correspondent university was founded.    

### Root node

First we define a `createTrieNode` function, which will allocate memory for a node, set it's paths to `NULL` and return it to a variable named `root`

```
TrieNode* root = createTrieNode();

TrieNode* createTrieNode()
{
    //Allocates memory for a trie node
    TrieNode* node = (TrieNode*)malloc(sizeof(TrieNode));

    //Sets children nodes to null
    for (int i = 0; i < 10; i++)
    {
        node -> paths[i] = NULL;
    }
    return node;
}
```

### Insert values

To insert values we creat a function which will take as arguments:
- A pointer to the `root` node
- A `char` array with the name of a university
- A `char` array with the year that university was founded

Adding the value consists of:
1. Seting the `root` node as the current node
2. Iterating through the `year` array, char by char
3. Getting the integer each char represents by subtracting it's ascii value by '0', and store it as a index.
4. Call `createTrieNode`, returning a new trie node to the `paths` pointers array on the index got on the last step.
5. Set the current node as the newly created node
6. Once the iteration ends, the `university` field of the last node created is filled.

```c
void insertTrie(TrieNode* root, char* year, char* university)
{
    TrieNode* current_node = root;

    for (int i = 0; year[i] != '\0'; i++)
    {
        int index = year[i] - '0';

        if (current_node -> paths[index] == NULL)
        {
            current_node -> paths[index] = createTrieNode();
        }
        current_node = current_node -> paths[index];
    }

    strcpy(current_node -> university, university);
}
```

It's basically creating a path, using each value of the `year` array as an amount of "steps" on each node, and then hiding a "treasure" there.

### Searching values
To search for values we create a function that takes as arguments:
- A `pointer` to the root node
- A `char` array `year`, which is our key


Searching for a value consists of
1. Seting the root node as our current node
2. Iterainng through every char of the `year` array
3. Getting the integer each char represents by subtracting it's ascii value by '0', and store it as a index
    - If the index on the `paths` array doesn't points to any node, returns "Not found".
4. Set the current node as the node just found with `index`
5. Once the iteration ends, return the value in the `university` field


```c
char *searchTrie(TrieNode *root, char* year)
{
    TrieNode* current_node = root;
    
    for (int i = 0; year[i] != '\0'; i++)
    {
        int index = year[i] - '0';
        
        if (current_node -> paths[index] == NULL)
        {
            return "Not found";
        }
        current_node = current_node -> paths[index];
    }

    return current_node -> university;
}
```

Every time we insert a new university using a year as key, we build a new path in our trie. That same path can be followed to get the value stored
