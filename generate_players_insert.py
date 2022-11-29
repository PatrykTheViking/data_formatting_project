import csv

valid_countries_list = ["Qatar", "Ecuador", "Senegal", "Netherlands", "England",  "Iran", "USA", "Wales", "Argentina",
                       "Saudi_Arabia", "Mexico", "Poland", "France", "Australia", "Denmark", "Tunisia", "Spain",
                       "Costa_Rica", "Germany", "Japan", "Canada", "Morocco", "Croatia", "Brazil", "Serbia", "Belgium",
                       "Switzerland", "Cameroon", "Portugal", "Ghana", "Uruguay", "South_Korea"]

country_id = 1

for country in sorted(valid_countries_list, key=str.lower):
    with open(fr'out_players_csv\out_players_{country}.csv', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)

        for row in csv_reader:
            print(f"INSERT INTO Zawodnicy (Nazwisko, Wiek, Pozycja, Zdjęcie, Narodowość) "
                    f"VALUES ('{row[1]}',{row[2]},'{row[4]}','{row[5]}',{country_id});")

        country_id += 1
