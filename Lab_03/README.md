# Assignment nr 2

## Task description

We will continue working with the publication data imported in Microproject 2. This time, you need to write a query that calculates the publication score for each employee as follows. The value of a given publication for each author is the number of points for that publication (column Points) divided by the number of authors (column Authors). An employee’s publication score is the sum of points from their 4 highest-value publications.

For example, if Kowalski published one paper worth 200 points with 9 co-authors, one paper worth 140 points with 1 co-author, and three solo-authored papers worth 200, 140, and 100 points, then the values of these publications for him are: 200/10=20, 140/2=70, 200/1=200, 140/1=140, and 100/1=100. Thus, his publication score is 200+140+100+70 = 510.

You should submit a single text file containing the CREATE and INSERT statements from the previous microproject along with one SELECT statement that executes the query described above.

## Contents
- `assignment3.sql` contains my solution to this assignment
- `csv_to_sql.py` is a script that creates solutions from provided csv files
