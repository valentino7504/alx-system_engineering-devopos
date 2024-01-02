#!/usr/bin/python3
'''
gets data from a REST API
'''
import requests
import sys


employee_id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/users/"
employee_details = requests.get(
    f"{url}{employee_id}"
).json()
employee_name = employee_details.get("name")
todos = requests.get(
    f"{url}{employee_id}/todos"
).json()
completed = 0
task_titles = []
for task in todos:
    if task.get("completed"):
        completed += 1
        task_titles.append(task.get("title"))
print(f"Employee {employee_name} is done with tasks" +
      f"({completed}/{len(todos)}):")
for title in task_titles:
    print(f"\t {title}")
