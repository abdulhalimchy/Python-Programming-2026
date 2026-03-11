# Write your solution here
from datetime import datetime

def final_points():
    start_times = {}

    # read start times
    with open("start_times.csv") as file:
        for line in file:
            name, time = line.strip().split(";")
            start_times[name] = datetime.strptime(time, "%H:%M")

    best_points = {}

    # read submissions
    with open("submissions.csv") as file:
        for line in file:
            name, task, points, time = line.strip().split(";")
            task = int(task)
            points = int(points)

            start = start_times[name]
            submit = datetime.strptime(time, "%H:%M")

            if (submit - start).total_seconds() > 3 * 3600:
                continue

            if name not in best_points:
                best_points[name] = {}

            if task not in best_points[name] or points > best_points[name][task]:
                best_points[name][task] = points

    results = {}

    for name in best_points:
        results[name] = sum(best_points[name].values())

    return results