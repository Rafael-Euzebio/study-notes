# Finance
[[CS50x Problem Sets]]

Implement a web app which allow users to register, "buy" and "sell" stocks

## Files

### app.py
- Flask and SQL imports
- Helper functions imports
- Disabling web cache
- Custom format to jinja to allow USD formatting easily
    - Done with `usd` function from `helpers.py`
- Flask config to store sessions in filesystem
- Routes to login and logout routes

### helpers.py
- `apology` function
    - Renders `apology.html`
- `login_required` function
    - Prevent users from acessing pages before logging in
- `lookup` function
    - Takes a symbol (e.g NFLX) as argument and returns a `dict` with the `name`, stock `price` and `symbol` of that company

### requirements.txt
- dependencies

### static/
- CSS files

### templates/
- `layout.html`
- `login.html`
- `apology.html`


## TODOS
- [x] `register` route
    - [x] Create `register.html`
        - [x] Require username input in a text field named `username`, render apology if there's no username
        - [x] Require password input in a text field named `password`
            - [x] Require the same password in a text field named `confirmation`
                - [x] Render apology if either field is blank or they're not the same
    - [x] Submit user input via `POST` to `/register`
    - [x] Insert user in database, storing a hash of the password 

- [x] `quote` route
    - [x] Create templates `quote.html` and `quoted.html` 
    - [x] Require user to input stock's symbol in a text field named `symbol`
    - [x] Submit to `quote` via `POST`
        - [x] `lookup` stock details
            - [x] Render it to `quoted.html`

- [ ] `buy` route
    - [ ] Require user to input stock's symbol in a text field named `symbol` using `lookup` to find its price, render apology if it's blank or invalid
    - [ ] Require user to input a number of shares, in a text field named `shares`. Render apology if it's not a positive integer
    - [ ] Submit to `/buy` via `POST`
    - [ ] Check how much cash the user still has
        - [ ] Render apology if user doesn't has enough cash
    - [ ] Create a table to keep track of how many shares the user has, at what price they were bought and when they were bought

- [ ] `index`
    - [ ] display a table of 
        - [ ] Which stocks the user has
        - [ ] The number of shares owned 
        - [ ] The total value of each (shares times price)
        - [ ] Current cash balance (stocks total plus cash)
- [ ] `sell`
    - [ ] Requires user to input stock symbol on a `select` menu.
    - [ ] Require user to input number of shares on a text field named `shares`
        - [ ] Render aology if the user does not own enough shares of that stock, or `shares` is not positive
    - [ ] Submit input via `POST` to `/sell`
    - [ ] Redirect to home page 
- [ ] `history`
    - [ ] Create a table that displays on each row
        - [ ] If a stock was bought or sold
        - [ ] The stock symbol
        - [ ] The price
        - [ ] The number of shares bought
        - [ ] The date and time it ocurred
- [ ] `personal touch`
    - [ ] Allow user to change passwords
    - [ ] Allow users to add cash to their account
    - [ ] Allow users to buy or sell stocks via `index`
    - [ ] Require passwords to have letters, numbers or symbols
