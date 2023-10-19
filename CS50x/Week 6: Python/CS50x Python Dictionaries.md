# Python Dictionaries
A dictionary is a [[CS50x Python Mappings Types]] used to hash keys and associate them to values

## Example
```py
pizzas = {
    "Cheese": 9,
    "Pepperoni": 10,
    "Buffalo Wing": 12,
    "Vegetales": 11
}

for topping, price in pizzas.items():
    print("A whole {} Pizza costs ${}".format(topping, price))
```
```
A whole Cheese Pizza costs $9
A whole Pepperoni Pizza costs $10
A whole Buffalo Wing Pizza costs $12
A whole Vegetales Pizza costs $11
```

On the above codeblock we: 
- create a dictionary named `pizzas`, each item containing a topping and a price (unnamed)  
    - The topping is used as a key to the prices
- Iterate through each topping and each price, and print it


