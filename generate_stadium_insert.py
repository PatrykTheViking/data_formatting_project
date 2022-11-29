import csv

with open('stadiums.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    stadium_id = 1

    for row in csv_reader:
        print(f'INSERT INTO Stadiony ("Nazwa turniejowa", Miasto, "Pojemność turniejowa") VALUES ('
              f"'{row[0]}','{row[1]}',{row[2]});")
        stadium_id += 1
