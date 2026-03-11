# Write your solution here
import urllib.request
import json

def retrieve_all():
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    courses = []

    for course in data:
        if course["enabled"]:
            total_exercises = sum(course["exercises"])
            courses.append((
                course["fullName"],
                course["name"],
                course["year"],
                total_exercises
            ))

    return courses


def retrieve_course(course_name: str):
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    weeks = len(data)
    students = 0
    hours = 0
    exercises = 0

    for week in data.values():
        students = max(students, week["students"])
        hours += week["hour_total"]
        exercises += week["exercise_total"]

    return {
        "weeks": weeks,
        "students": students,
        "hours": hours,
        "hours_average": hours // students,
        "exercises": exercises,
        "exercises_average": exercises // students
    }