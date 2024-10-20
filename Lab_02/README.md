# Assignment nr 2

## Task description

Attached are three CSV files containing data about employees of the Institute of Computer Science and their publications from 2017 to 2020. The task is to create three tables (Author, Work, Authorship) with appropriate columns, insert the data from the corresponding CSV files into them, and then write (using a query) the following pairs of employees (IDs): for each employee with a risk of 1 who has not published any work in 2020, list all employees with whom they have ever published a joint work.

You need to submit a single text file containing:

- Three CREATE TABLE statements (to create the tables)
- A series of INSERT statements (to insert the data)
- One SELECT statement (the query)
- 
The file must execute correctly when loaded with the command:

SQL> @file_to_load.sql

in Oracle database (similarly for PostgreSQL).

## Contents
- `assignment2.sql` contains my solution to this assignment
- `csv_to_sql.py` is a script that creates solutions from provided csv files
