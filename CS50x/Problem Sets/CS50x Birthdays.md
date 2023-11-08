# Birthdays
[[CS50x Problem Sets]]

## Files

### app.py
- Flask application
    - `/` route
        - `POST` and `GET` requests
            - `GET` renders `index.html`
            - `POST` redirects to `/` via `GET`

### birthdays.db
- Table birthdays with 4 columns
    - id
    - name
    - month
    - day

### index.html
- Rendered by flask

## TODOS
- [x] Display table in `index.html` when `/` is requested via `GET`
    - [x] Query the `birthdays` database
    - [x] Render in `index.html`
- [x] Add new birthdays to database when `/` is requested via `POST`
    - [x] Add a HTML form to input name, month and day
    - [x] Insert the form info in database

