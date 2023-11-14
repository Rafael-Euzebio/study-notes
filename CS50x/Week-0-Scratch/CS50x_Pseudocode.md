# Pseudocode

Pseudocode is a way to represent the steps of [Algorithms](./CS50x_Algorithms.md) using  plain language (e.g English), in steps, instead of a programming language. 

It is intended for human reading, and is a way to simplify an algorithm. 

## Example
(This example references the third algorithm used in [Algorithms](./CS50x_Algorithms.md)).
1. Pick up phone book
2. Open to the middle of the phone book
3. Look at page
4. If person is on page
	1. Call person
 5. Else if person is earlier in book
	1. Open to middle of left half of book
	2. Go back to line 3
6. Else if person is later in book
	1. Open to middle of right half of book 
	2. Go back to line 3
7. Else 
	1. Quit

### Key points
The pseudocode above was written with specific words in mind, to reference real code.

- Some lines begins with verbs like *pick up*, *open*, *look at*. These are equivalent to *functions*.
- Some lines include statements like `if` or `else if`. These are called *conditionals*
- Some expressions can be stated as *true* or *false*, such as "person is earlier in the book". We call these *boolean expressions*
- Finally, there are statements like "go back to line 3". We call these *loops*

## Advantages
Pseudocode is an important skill for at least two reasons.

- When you pseudocode before creating formal code, it allows you to think through the logic of your problem in advance

- When you pseudocode, you can later provide this information to others that are seeking to understand your coding decisions and how your code works


