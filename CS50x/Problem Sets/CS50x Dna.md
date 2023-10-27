# DNA
- Dna is a sequence of nucleotides
    - Each nucleotide has one of four bases:
        - adenine (A)
        - cytosine (©)
        - guanine (G)
        - thymine (T)
    - Some portions of the sequence are the same or very similar across all humans
        - Other portions vary across the population
            - These portions are called Short Tandem Repeats STR
                - That portion repeats several times at specific locations of the DNA
            - The chance two different person have one same STR is small
                - The chance they have two exact STR is even smaller
                    - Comparing multiple STR improve the accuracy of DNA profiling


## Database 
|  name   | AGAT | AATG | TATC |
|---------| ---- | ---- | ---- |
| Alice   |  28  |  42  |  14  |
| Bob     |  17  |  22  |  19  |
| Charlie |  36  |  18  |  25  |
             
- Alice has the sequence AGAT repeated 28 times somewhere in her DNA
    - Bob has the same sequence repeated 17 times
    - ....
- WHen analyzing a DNA, if the amount of times the sequences repeats match someone in the table, it's evidence that it belongs to that person


## Files

### dna.py
- [x] Require arguments:
    - csv file with STR counts (list of individuals)
    - DNA text file with a sequence to identify

- [x] Load the csv file and read its contents
- [x] Load the DNA file and read its contents
- [ ] For each of the STR call `longest_match` to get how many times each STR repeats in the DNA
    - [ ] If the values returned match someone in the CSV files, print the name
