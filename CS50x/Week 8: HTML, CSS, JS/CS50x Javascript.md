# Javascript
Javascript is a [[ST Multiparadigm]] and [[Univesp Objects Oriented Programming]] [[CS50x Programming Language]]

It is mostly used in [[ST Frontend]] Programming along with [[CS50x HTML]] and [[CS50x CSS]]

Its purpose is to give logical functionality to a website

## Syntax
Javascript syntax has similarties with C an somewhat with Python, allowing us to use english-like syntax

```javascript
var nums = [1, 2, 3, 4, 5, 6];

console.log(nums);

for (var number of nums)
{
    console.log(number * 2)
}
```

outputs every `number` in `nums`

The nums array is also an object, it has methods like `nums.size()`, `nums.pop()`, `nums.push(x)`...

Arrays also has a `.map()` method which allows us to call an [[CS50x Anonymous Functions]] to every element in a array

## Events
Javascript interacts with HTML and CSS through Events.  
Events allows us to execute functions when something happens in the page, like a click of a button, or a page refresh

### Example
```html
    <body>
        <button onclick="alertName(event)">Button 1</button>
        <button onclick="alertName(event)">Button 2</button>
    </body>

```
```javascript
function alertName(event) {
    var button = event.srcElement;
    alert('You clicked on ' + button.innerHTML)
} 
```

`onclick` is an event, when the button is clicked it calls the `alertName()` function, which takes the event object as an argument.  
Then it extracts the Element name from the object and creates an alert with the HTML text that's inside the object
