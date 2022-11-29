import csv

valid_countries = ["Qatar", "Ecuador", "Senegal", "Netherlands", "England",  "Iran", "USA", "Wales", "Argentina",
                       "Saudi-Arabia", "Mexico", "Poland", "France", "Australia", "Denmark", "Tunisia", "Spain",
                       "Costa-Rica", "Germany", "Japan", "Canada", "Morocco", "Croatia", "Brazil", "Serbia", "Belgium",
                       "Switzerland", "Cameroon", "Portugal", "Ghana", "Uruguay", "South-Korea"]

with open('out_countries.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    for row in csv_reader:
        if row[0] in valid_countries:
            print(f"INSERT INTO Kraje (Nazwa, Kod, Flaga) VALUES ('{row[0]}','{row[1]}','{row[2]}');")
