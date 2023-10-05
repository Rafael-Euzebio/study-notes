# Speller
[[Problem Sets]]

## Asymptotically Time vs Wall-Clock Time
- An algorithm's time complexity is described by the dominant term
    - Linear time complexity is described as $O(n)$
        - Even if it's $O(2n)$, that's still linear time, the `2` is removed and it is described as just $O(n)$, since `n` could be much larger than two
            - But in reality, $O(2n)$ feels *twice* as slow as $O(n)$ 
            - The challenge is to create the fastest spell checker possible, in "wall-clock" time, not asymptotic time

## Files            
### dictionary.h 
- `if` syntax that checks if this header file was already defined, to ensure the compiler doesn't defines it more than once
    ```c
    #ifndef DICTIONARY_H     
    #define DICTIONARY_H
    /// code
    #endif
    ```
- `#define` `LENGTH` as `45`
    - This is not considered a *constant variable*, instead it's an *alias*

- Function prototypes:
    - Three of them takes `char *` as an argument (in other words, a `string`)
        - The arguments are `constants`, they can't be changed inside the `function's` scope
            - `bool check(const char *word);`
            - `unsigned int hash(const char *word);`
            - `bool load(const char *dictionary);` 
    - The other one is `bool unload(void);`


### dictionary.c
- `struct` *node* which represents a node in a hash table
    - char array of `LENGTH` + 1
    - `pointer` to the next node
- table array of size `N` which represents a hash table
    - `N` = 26
- Functions `load` `check`, `size`, `unload`
    - Implemented just enough for the code to compile

### speller.c
- `check`, `load`, `size` and `unload` functions are benchmarked through `getrusage` function

- Usage is `speller [dictionary] text`
    - `dictionary` must be a file containing a list of lowercase words, one per line
        - It is optional, by default `speller` will user `dictionaries/large`
            - It has 143,091 words
                - One word per lien
                - No word is longer than 45 characters
                - No word appears more than once
            - `dictionaries/small` can also be used, for easier debugging
    - `text` is a file to be spell-checked

### texts
- A bunch of `txt` files from different sources
- Loading those files through `./speller text` will produce as output
    - All mispelled words
    - The amount of mispelled words
    - The amount of words in dictionary
    - The amount of words in text
    - Time in seconds that it took to execute each function
    - Total time

### Makefile
- This file tells `make` how to compile your code when it has multiple files
    1. The first line tells `make` to execute the next lines when `make` or `make speller` is executed
    2. The second line tells `make` to compile `speller.c` into machine code `speller.o`
    3. The third line tells `make` to compile `dictionary.c` into machine code `dictionary.o`
    4. The fourth line tells `make` to link `speller.o` and `dictionary.o` into a single file called `speller`

## Specification
- `speller.c` or `Makefile` must not be altered
- `dictionary.c` must have it's functions implemented
    - The function prototypes must not be altered
    - New functions and variables can be added
    - The value of `N` can be changed
- `dictionary.h` can be altered, but not the functions prototypes
- `check` function must: 
    - be case-insentive
    - return `true` if a word is in the `dictionary`
- Assuem that `dictionary`:
    - Is alphabetically sorted
    - Has one word per line
    - No word is longer than `LENGTH`
- The program must not leak memory


## TODO
- [ ] Implemente `load`
- [ ] Implement `hash`
- [ ] Implement `size`
- [ ] Implement `check`
- [ ] Implement `unload`
