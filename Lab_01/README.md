# Assignment nr 1

## Task description

Attached is a CSV file containing a dataset of publications by employees of the Institute of Computer Science from 2017 to 2020. The task is to: create a table with appropriate columns; insert the data into it; write (using a query) all works published in 2020, where the average number of points per author is 100 or more, sorted by the number of authors; and finally, drop the created table.

You need to submit a single text file containing:
- One CREATE TABLE statement (to create the table)
- A series of INSERT statements (to insert the data)
- One SELECT statement (the query)
- One DROP TABLE statement (to delete the table)

The file must execute correctly when loaded with the command

SQL> @file_to_load.sql

in Oracle database (similarly for PostgreSQL).

## Contents
- `Publikacje.sql` contains my solution to this assignment
- `pyhtonScript.py` is a script for inserting data from csv into sql file
