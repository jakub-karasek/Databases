import csv

output_file = 'assignment3.sql'
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
WITH pub_point AS (
    SELECT 
        p.id AS publication_id, 
        (p.points / p.authors) AS pub_points
    FROM 
        PUBLICATIONS p 
),
ranked_points AS (
    SELECT 
        a.author,
        pp.pub_points,
        ROW_NUMBER() OVER (PARTITION BY a.author ORDER BY pp.pub_points DESC) AS rn
    FROM 
        AUTHORSHIP a
    LEFT JOIN 
        pub_point pp ON a.publication = pp.publication_id
)
SELECT 
    rp.author,
    COALESCE(SUM(rp.pub_points), 0) AS total_points
FROM 
    ranked_points rp
WHERE 
    rp.rn <= 4
GROUP BY 
    rp.author
ORDER BY 
    total_points;
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



