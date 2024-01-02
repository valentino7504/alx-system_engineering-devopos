#!/usr/bin/python3
"""
This module is used to get a response from a REST API
It gets the todo list of an employee with a specific ID
The ID is accepted via argv
Requests are made using the requests module
"""
import requests
import sys
if __name__ == "__main__":
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
