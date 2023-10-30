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
