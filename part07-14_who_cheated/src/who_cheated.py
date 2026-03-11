# Write your solution here

from datetime import datetime

def cheaters():
    start_times = {}

    # read start times
    with open("start_times.csv") as file:
        for line in file:
            name, time = line.strip().split(";")
            start_times[name] = datetime.strptime(time, "%H:%M")

    cheater_list = set()

    # read submissions
    with open("submissions.csv") as file:
        for line in file:
            name, task, points, time = line.strip().split(";")
            submission_time = datetime.strptime(time, "%H:%M")

            start_time = start_times[name]
            diff = submission_time - start_time

            if diff.total_seconds() > 3 * 3600:
                cheater_list.add(name)

    return list(cheater_list)