# Seven Day Average
[Problem Sets](./CS50x_Problem-Sets.md)

- Covid cases are tracked using a 7-day average
- NYT tracks daily cases in a CSV file
    - The file is requested and stored in a CSV file
        - The cases must be selected by user by state and stored in a list `states`

## Functions TODO
### calculate
- [x] create dictionary `new_cases` to track last 14 days of new COVID cases for each state
    - Keys must be the name of the states
    - Values must be most recent 14 days 
        - A second dictionary `previous_cases` is necessary to keep track of each day new's cases as it's calculated
    - return must be the `new_cases` dictionary

### comparative_average
- [x] Get a 7-day average for the selected state
    - [x] Get a 7-day average for the previous week
        - [x] Calculate the difference in percentage of the two
