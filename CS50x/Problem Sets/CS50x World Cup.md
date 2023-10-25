# World Cup
[[Problem Sets]]

- In soccer Word Cup, the knockout consists of 16 teams
    - Each team has a FIFA Rating, which represents the team's skill
        -   It's possible to estimate which team will win the tournament by their ratings
            - To do that we need to simulate the tournament thousands of times

## Files

### 2018m.csv
- 16 teams in knockout of 2018 Men's World Cup
- Rating of each team
- Each team will play against the one in the next line of the file
    - The winner of the match between team in line 1 and 2 will play against the winner from line 3 and 4 and so on...
- Each team with their rating can be represented in a dictionary
    - `{"team": "Uruguay", "rating:" 976}`

### 2019w.csv
- Same as 2018m.csv

### tournament.py
- N variable represents amount of similutations, 1000

### Functions
- `simulate_game`
    - Takes two teams as input and simulates a game
    - If the first team wins, returns `True`, otherwise, `False`

- `simulateround`
    - Takes a list of teams as argument
        - simulates games between each pair
        - Returns a list of all teams that won the round

- `main`
    - Ensure one of the command lines arguments is a csv file
    - list `teams`
        - teams not assigned
    - dictionary `counts`
        - will associate how many times a team has won a simulated tournament
    - sorts team in descending order according to `counts`
    - prints the estimated probability that each team wins the World Cup

## TODOS
- `main`
    - [ ] Open csv file provided by user
    - [ ] Read csv file as a dictionary
    - [ ] Convert ratings to integer
    - [ ] Add each team and its ratings to `teams` list
