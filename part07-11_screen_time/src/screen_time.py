# Write your solution here
from datetime import datetime, timedelta

filename = input("Filename: ")
start_date_input = input("Starting date: ")
days = int(input("How many days: "))

start_date = datetime.strptime(start_date_input, "%d.%m.%Y")

print("Please type in screen time in minutes on each day (TV computer mobile):")

entries = []
total_minutes = 0

for i in range(days):
    current_date = start_date + timedelta(days=i)
    date_str = current_date.strftime("%d.%m.%Y")

    data = input(f"Screen time {date_str}: ")
    tv, computer, mobile = map(int, data.split())

    total_minutes += tv + computer + mobile
    entries.append(f"{date_str}: {tv}/{computer}/{mobile}")

end_date = start_date + timedelta(days=days - 1)
average = total_minutes / days

with open(filename, "w") as file:
    file.write(f"Time period: {start_date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}\n")
    file.write(f"Total minutes: {total_minutes}\n")
    file.write(f"Average minutes: {average}\n")
    
    for entry in entries:
        file.write(entry + "\n")

print(f"Data stored in file {filename}")