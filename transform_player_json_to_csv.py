import json
import csv

valid_countries_list = ["Qatar", "Ecuador", "Senegal", "Netherlands", "England",  "Iran", "USA", "Wales", "Argentina",
                       "Saudi_Arabia", "Mexico", "Poland", "France", "Australia", "Denmark", "Tunisia", "Spain",
                       "Costa_Rica", "Germany", "Japan", "Canada", "Morocco", "Croatia", "Brazil", "Serbia", "Belgium",
                       "Switzerland", "Cameroon", "Portugal", "Ghana", "Uruguay", "South_Korea"]

for file in valid_countries_list:
    with open(fr'C:\Users\Patryk\PycharmProjects\APIProject\out_players_json\out_players_{file}.json',
              encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    data_file = open(fr'C:\Users\Patryk\PycharmProjects\APIProject\out_players_csv\out_players_{file}.csv',
                     'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(data_file)

    count = 0
    for data in json_data:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1

        csv_writer.writerow(data.values())

    data_file.close()
