# GDB
GDB (GNU Debugger) is a debugger (or [[CS50x Debugging]] tool) used to debug several programming languages, like [[C],] C++, Rust and others.

## Commands
GDB is a command-line tool and can be started with
```
gdb (program)
```

the `program` must have been compiled with a debug flag like:

```
gcc -g (program)
```
for *C* programs

### Basic Commands

- #### tui enable    
    `tui enable`  
     Allows code and breakpoints view while debugging, can be used with the `-tui` flag

- #### run
    `run [argument]` or `r [argument]`
    runs the program with the specified arguments

- #### break
    ```
    break [Function Name]
    break [Line Number]
    break [File Name]:[Line Number]
    break [...] if [condition]
    b [...]
    ```
    Creates a break point at a specific line, function or address.   
    Can also be used with a if condition, only stopping if that condition evaluates to `true`.

- #### next
    ```
    next
    next [count]
    n
    ```
    Continues to the next line of code or the specified `count` argument without stopping on function calls.

- #### step
    ```
    step
    step [count]
    s
    ```
    Continues to the next line of code, stepping into function calls, or the specified `count` argument.   

- #### list
    ```
    l
    list [line number]
    list [function]
    list -
    ```
    Prints the lines around the last line printed. If a line was printed before executing `list` from the `step` or `next` command, `list` prints the 10 lines around the current line (5 above and 5 below), if the lines was printed through `list [line number]` or `list [function]` then `list` will print the lines around the lines printed before.

- #### print
    ```
    p
    print [expression]
    print [$ Previous value number]
    ```
    Prints the specified variable, address, register or result of a expression.  Printed values are saved in gdb history, and a value starting from `1`. These values can be referenced later with `$(number)`.

- #### up/down
    ```
    up
    down
    up [count]
    down [count]
    up [function name]
    down [function name]
    ```
    Moves between the stack frame, allowing the programmer to select a previous function and analyze the contents of variables, adressess etc...inside the scope of that function, and go back to the executing function at any time.

- #### display/undisplay
    ```
    display [expression]
    undisplay [expression number]
    ```
    Prints the expression specified after each step, allowing the programmer to have the values of a variable, address etc...always in display.
    To stop printing the `undisplay` command must be used, but instead of taking the variable name as an argument, it takes the ID assigned to that display, which is printed after each display

    ```
    (gdb) display a
    2: a = 1
    (gdb) undisplay 2
    ```

- #### watch
    ```
    watch [expression] 
    ```
    Stops the program execution everytime the specified expression's value changes.  

- #### backtrace
    ```
    bt
    backtrace  
    backtrace [option] [count]
    ``` 
    Backtrace prints the current call stack, it has many functions but the most importante are:
    - `count` prints the innermost frames
    - `-count` prints the outermost frames
    - `full` prints the stack and the the local variables of each function

- #### continue
    ```
    continue
    continue [ignore count]
    ```
    Runs the program until it reaches a breakpoint or the end of it. The `ignore count` argument will ignore the next n-1 times when the current breakpoint is reached. This is particularly useful with recursive functions

- #### finish
    ```
    fin
    finish
    ```
    Runs the program until the selected function returns and prints the returned value


- #### info
    ```
    info [argument]
    info locals
    info breakpoints
    ....
    ```
    Displays information about the specified argument, that may be variables, breakpoints, registers, addresses and much more...

- #### delete
    ```
    d
    delete 
    delete [breakpoint number]
    ```
    Deletes all breakpoints or only the specified one, the `breakpoint number` can be get through `info breakpoints`

- #### whatis
    ```
    what [expression]
    what is [expression]
    ```
    Prints the data type of `expression`

### Advanced Commands
- #### target record-full
    ```
    target record-full
    record full
    ```
    Records the program execution, logging the information of variables, functions executed etc.  
    That command allows *Reverse Execution*, the use of the commands `reverse-next`, `reverse-step`, `reverse-continue` and `reverse-finish`, which does the same thing as the original commands, but reversely.

- #### set var
    ```
    set var [expression]
    ```
    Assings a value to the specified value.  
