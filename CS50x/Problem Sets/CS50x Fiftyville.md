# Fiftyville

- Find through SQL queries:
    - Who stole the cs50 duck
    - What city the thief escaped to
    - Who helped the thief escape
- The theft took place in July 28, 2021 on Humphrey Street
- Document every query executed in `log.sql`

## Tables
### `crime_scene_reports`
- id
- year
- month
- day
- street
- description

### `interviews`
- id
- name
- year
- month
- day
- transcript
 
### `atm_transactions`
- id
- account_number
- year
- month
- day
- atm_location
- transaction_type
- amount

### `bank_accounts`
- account_number
- person_id (reference to id in `people`)
- creation_year

### `airports`
- id
- abbreviation
- full_name
- city

### `flights`
- id
- origin_airport_id (reference to id in `airports`)
- destination_airport_id (reference to id in `airports`)
- year
- month
- day
- hour
- minute

### `passengers`
- flight_id (reference to id in `flights`)
- passport_number
- seat

### `phone_calls`
- id
- caller
- receiver
- year
- month
- day
- duration

### `people`
- id
- name
- phone_number
- passport_number
- license_plate

### `bakery_security_logs`
- id
- year
- month
- day
- hour
- minute
- activity
- license_plate

## Notes
### Witnesses
- Theft of CS50 duck happened at 10:15am at the bakery. 3 witnesses
    - Witness 1 saw the thief get into a car in the bakery parking lot betwen 10:15am and 10:25am
    - Witness 2 recognized the thief as someone who withdrawed money on at the ATM on Legget Street
    - Witness 3 heard the thief talking with someone about taking the earliest flight out of fiftyville

### Bakery
- Activity on the parking lot between 10:15am and 10:25am

| id  | activity | license_plate | hour | minute |
|-----|----------|---------------|------|--------|
| 260 | exit     | 5P2BI95       | 10   | 16     |
| 261 | exit     | 94KL13X       | 10   | 18     |
| 262 | exit     | 6P58WS2       | 10   | 18     |
| 263 | exit     | 4328GD8       | 10   | 19     |
| 264 | exit     | G412CB7       | 10   | 20     |
| 265 | exit     | L93JTIZ       | 10   | 21     |
| 266 | exit     | 322W7JE       | 10   | 23     |
| 267 | exit     | 0NTHK55       | 10   | 23     |


### ATM on Leggett Street
- Activity on ATM on Leggett Street on that day

| id  | account_number | transaction_type | amount |
|-----|----------------|------------------|--------|
| 246 | 28500762       | withdraw         | 48     |
| 264 | 28296815       | withdraw         | 20     |
| 266 | 76054385       | withdraw         | 60     |
| 267 | 49610011       | withdraw         | 50     |
| 269 | 16153065       | withdraw         | 80     |
| 275 | 86363979       | deposit          | 10     |
| 288 | 25506511       | withdraw         | 20     |
| 313 | 81061156       | withdraw         | 30     |
| 336 | 26013199       | withdraw         | 35     |

#### People who withdrawed money on that day

|   id   |  name   |  phone_number  | passport_number | license_plate | account_number |
|--------|---------|----------------|-----------------|---------------|----------------|
| 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       | 49610011       |
| 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       | 26013199       |
| 458378 | Brooke  | (122) 555-4581 | 4408372428      | QX4YZN3       | 16153065       |
| 395717 | Kenny   | (826) 555-1652 | 9878712108      | 30G67EN       | 28296815       |
| 396669 | Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       | 25506511       |
| 467400 | Luca    | (389) 555-5198 | 8496433585      | 4328GD8       | 28500762       |
| 449774 | Taylor  | (286) 555-6063 | 1988161715      | 1106N58       | 76054385       |
| 438727 | Benista | (338) 555-6650 | 9586786673      | 8X428L0       | 81061156       |

**And were also at the bakery during the theft**

|   id   | name  |  phone_number  | passport_number | license_plate |
|--------|-------|----------------|-----------------|---------------|
| 396669 | Iman  | (829) 555-5269 | 7049073643      | L93JTIZ       |
| 467400 | Luca  | (389) 555-5198 | 8496433585      | 4328GD8       |
| 514354 | Diana | (770) 555-1861 | 3592750733      | 322W7JE       |
| 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |


#### Phone calls that lasted less than 60s from people who were at the bakery and withdrawed money

| id  | name  |     caller     |    receiver    | year | duration | passport_number | license_plate |
|-----|-------|----------------|----------------|------|----------|-----------------|---------------|
| 233 | Bruce | (367) 555-5533 | (375) 555-8161 | 2021 | 45       | 5773159633      | 94KL13X       |
| 255 | Diana | (770) 555-1861 | (725) 555-3243 | 2021 | 49       | 3592750733      | 322W7JE       |


### People who were on flight 35, were at the crime scene and did transactions

|   id   | name  |  phone_number  | passport_number | license_plate |
|--------|-------|----------------|-----------------|---------------|
| 467400 | Luca  | (389) 555-5198 | 8496433585      | 4328GD8       |
| 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |



## What city the thief fled to?
Dallas

## Who stole the cs50 duck?
### Suspects

|   id   | name  |  phone_number  | passport_number | license_plate |
|--------|-------|----------------|-----------------|---------------|
| 396669 | Iman  | (829) 555-5269 | 7049073643      | L93JTIZ       |
| 467400 | Luca  | (389) 555-5198 | 8496433585      | 4328GD8       |
| 514354 | Diana | (770) 555-1861 | 3592750733      | 322W7JE       |
| 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
