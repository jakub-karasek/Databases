import csv

output_file = 'assignment2.sql'
sqlfile = open(output_file, 'w', encoding='utf-8')

# CREATE TABLE SECTION

table = """CREATE TABLE PUBLICATIONS (
    ID INT,
    TITLE VARCHAR(200),
    YEAR INT,  
    AUTHORS INT,
    POINTS INT
);\n\n"""

sqlfile.write(table)

table = """CREATE TABLE AUTHORS (
    ID VARCHAR(50),
    RISK INT,
    SLOTS DECIMAL(3,2)  
);\n\n"""

sqlfile.write(table)

table = """CREATE TABLE AUTHORSHIP (
    PUBLICATION INT,
    AUTHOR VARCHAR(50)  
);\n\n"""

sqlfile.write(table)

# INSERT SECTION

# INSERTING DATA FROM PRACE.CSV

input_file = 'Prace.csv'  
 
with open(input_file, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        id = row['ID']
        title = row['Tytuł'].replace("'", "''")  
        title = title.replace("&", "' || CHR(38) || '")  
        year = row['Rok']
        authors = row['Autorzy']
        points = row['Punkty']
        insert = f"INSERT INTO PUBLICATIONS (ID, TITLE, YEAR, AUTHORS, POINTS) VALUES ({id}, '{title}', {year}, {authors}, {points});\n"
        sqlfile.write(insert)

sqlfile.write("\n")

# INSERTING DATA FROM AUTORZY.CSV

input_file = 'Autorzy.csv'  

with open(input_file, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        id = row['ID']
        risk = row['Ryzyko']
        slots = row["Sloty"].replace("\"", "")
        slots = slots.replace(",", ".")

        insert = f"INSERT INTO AUTHORS (ID, RISK, SLOTS) VALUES ('{id}', {risk}, {slots});\n"
        sqlfile.write(insert)

sqlfile.write("\n")

# INSERTING DATA FROM AUTORSTWO.CSV

input_file = 'Autorstwo.csv'  

with open(input_file, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        publication = row['Praca']
        author = row['Autor']

        insert = f"INSERT INTO AUTHORSHIP (PUBLICATION, AUTHOR) VALUES ({publication}, '{author}');\n"
        sqlfile.write(insert)

sqlfile.write("\n")

# SELECT SECTION

query = """
SELECT DISTINCT 
    p1.id AS pracownik, 
    p2.AUTHOR AS partner
FROM 
    AUTHORS p1
JOIN 
    AUTHORSHIP a1 ON p1.id = a1.author
JOIN 
    AUTHORSHIP p2 ON a1.publication = p2.publication 
    AND a1.author <> p2.author
WHERE 
    p1.risk = 1 
    AND p1.id NOT IN (
        SELECT DISTINCT 
            author 
        FROM 
            AUTHORSHIP D 
        JOIN 
            PUBLICATIONS ON D.publication = PUBLICATIONS.id 
        WHERE 
            year = 2020
    );


\n
"""
sqlfile.write(query)

# DROP TABLE SECTION

table = "DROP TABLE PUBLICATIONS;\n"
sqlfile.write(table)

table = "DROP TABLE AUTHORS;\n"
sqlfile.write(table)

table = "DROP TABLE AUTHORSHIP;\n"
sqlfile.write(table)

sqlfile.close()
