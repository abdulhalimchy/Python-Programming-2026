# tee ratkaisu tänne
# Write your solution here

import math

def get_station_data(filename: str):
    stations = {}

    with open(filename) as file:
        next(file)  # skip header
        for line in file:
            parts = line.strip().split(";")
            longitude = float(parts[0])
            latitude = float(parts[1])
            name = parts[3]

            stations[name] = (longitude, latitude)

    return stations


def distance(stations: dict, station1: str, station2: str):
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2

    return math.sqrt(x_km**2 + y_km**2)


def greatest_distance(stations: dict):
    station_names = list(stations.keys())

    max_distance = 0
    station_a = ""
    station_b = ""

    for i in range(len(station_names)):
        for j in range(i + 1, len(station_names)):
            s1 = station_names[i]
            s2 = station_names[j]

            d = distance(stations, s1, s2)

            if d > max_distance:
                max_distance = d
                station_a = s1
                station_b = s2

    return station_a, station_b, max_distance