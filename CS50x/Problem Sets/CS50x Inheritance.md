# Inheritance
[[CS50x Problem Sets]]

## Combinations
- A person's blood type is determined by two alleles
    - Each allele can be A, B or O
        - This gives 9 possible combinations
            - OO
            - OB
            - AO
            - AA
            - AB
            - BO
            - BA
            - BB
        - Each alelle comes from one parent
            - AO + BB = AB or OB
            - AO + OB = AO or OB or AB or OO

## Files
### inheritance.c
- `struct person`
    - Each `person` has an array of two `parents`
        - A `parent` is a pointer to another `person`
    - Each person has an array of two `alleles`
        -   An `alelle` is a char, either `A`, `B` or `O`

#### Functions
- `main`
    - Seeds a random number generator with the current time
    - Calls `create_family` to create a family of 3 generations
        - TODO
    - Calls `print_family`
    - Calls `free_family` to `free` any memory previously allocated
        - TODO

- `create_family` 
    - Takes an integer (`generatiosn`)
        - Must allocate one `person` for each member of the family of that number of generations
            - `create_family(3)` should return a pointer to a person with two parents. Each parent also has two parents
        - Each `person` should have `alleles`. 
            - The oldest generation has random alleles (`random_alelle` function)
            - Youngers generations should inherit one alelle from each parent, randomically
            - Each `person` should have two parents, except the oldest generation
                - `parents` is an array of two pointers, one for each parent


### TODO

#### create_family
- [x] Allocate memory for a new person
- [x] Create parents recursively
- [x] Set parents pointers in case `generation > 1` and assign alleles
- [x] Set parents pointers to NULL in case `generations == 1` and get alleles randomically
- [x] Return a pointer for the `person` that was allocated

#### free_family
- [x] `free` parents recursively, and then `free` child 
