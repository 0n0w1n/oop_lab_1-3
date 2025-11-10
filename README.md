# What is this lab about?
- why we should use lambda.
- using OOP in the program.
- how we work and associate with other poeple with github.

# Project structure
In this project we have 3 files
- README.md
    - it's like the description of the project for more understanding
- Cities.csv
    - It's a raw data of cities information for using in main program.It contain countries cities temperature and position
- data_processing.py
    - This file is main program for this project

# Detailed explanation of each class, detailing attributes and key methods
- class Dataloader
    - stores the starting directory for locating data files
    - Load a CSV file and return its contents as a list of dictionaries
- class Table
    - attribute : list of dict objects it's data storage for the class. It holds the collection of cities
    - key methods : 
        - init(self, cities)
            - storing the input list of cities in the self.cities
        - filter(self, condition)
            - filter cities with the condition
        - aggregate(self, aggregation_function, aggregation_key)
            - calculates a single summary value
        - table(self)
            - return list of cities in object

# How to test and run your code
run the code with Cities.csv file in directory and look at the output.ff the code runs successfully and the Cities.csv file is found, the output printed to the console correctly