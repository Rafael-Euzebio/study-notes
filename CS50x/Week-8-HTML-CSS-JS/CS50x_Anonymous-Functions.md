# Anonymous Functions
An anonymous function is a function that does not has a identifier. These functions are referenced through a variable or given as arguments to another functions  

An anonymous function referenced through a variable can be called through that variable. The return value from that function is stored in the variable
A function that takes an anonymous function as argument is called a *High-Order Function*
An anonymous function is executed when its high-order function is called

## Example
```javascript

var test = function () {
    var a = 1;
    var b = 2;
    return a + b;
}

test(); /// calls anonymous function
console.log(test) /// 3
```

`test()` calls the anonymous function and its return value is stored in `test` 

```javascript
var nums = [1, 2, 3, 4, 5, 6];

var double_nums = nums.map(function(num) {
    return num * 2;
})

console.log(double_nums);
```
The anonymous function is created in the `.map` method. It is automatically called when `nums.map` is executed

An anonymous function is useful when we don't plan to reuse a function
