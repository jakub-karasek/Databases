import csv
 
# Ścieżka do pliku CSV z danymi
input_file = 'Publikacje.csv'  # Upewnij się, że plik znajduje się w tym samym katalogu co skrypt
output_file = 'insert_publications.sql'
 
with open(input_file, 'r', encoding='utf-8') as csvfile, open(output_file, 'w', encoding='utf-8') as sqlfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        id = row['ID']
        title = row['Tytuł'].replace("'", "''")  # Escaping pojedynczych cudzysłowów
        year = row['Rok']
        authors = row['Autorzy']
        points = row['Punkty']
        insert = f"INSERT INTO PUBLICATIONS (ID, TITLE, YEAR, AUTHORS, POINTS) VALUES ({id}, '{title}', {year}, {authors}, {points});\n"
        sqlfile.write(insert)
 
print(f'Polecenia INSERT zostały zapisane w pliku {output_file}')
