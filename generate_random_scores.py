import random
import time

team_range = list(range(1, 33))
random.shuffle(team_range)


def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d', prop)


for host in team_range:
    for guest in team_range:
        city_range = random.randint(1, 8)
        score_range = random.choice([1, 2, 0])
        if host == guest:
            continue
        else:
            print(f'INSERT INTO Mecze (Gospodarz, Gość, Wynik, Miejsce, "Data rozpoczęcia") VALUES ({host}, '
                  f"{guest}, {score_range}, {city_range},"
                  f" '{random_date('2022-11-19', '2022-12-18', random.random())}');")
