#!/usr/bin/python3
'''
This module is used to extract API responses and
export them to a JSON
'''
import json
import requests
import sys
if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/"
    employee_details = requests.get(
        f"{url}{employee_id}"
    ).json()
    username = employee_details.get("username")
    todos = requests.get(
        f"{url}{employee_id}/todos"
    ).json()
    task_list = []
    for task in todos:
        task_list.append(
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
        )
    todo_list = {f"{employee_id}": task_list}
    with open(file=f"{employee_id}.json", mode="w") as file:
        json.dump(todo_list, file)
