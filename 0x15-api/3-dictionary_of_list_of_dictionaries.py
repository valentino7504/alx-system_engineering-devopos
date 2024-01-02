#!/usr/bin/python3
"""
This module is used to get a response from a REST API
It gets the todo list of all employees
Requests are made using the requests module
"""
import json
import requests
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(
        f"{url}"
    ).json()
    all_users_dict = {}
    for user in users:
        todo_list = requests.get(
            f"{url}/{user.get('id')}/todos"
        ).json()
        task_list = [
            {
                "username": f"{user.get('username')}",
                "task": f"{task.get('title')}",
                "completed": task.get("completed")
            }
            for task in todo_list
        ]
        all_users_dict[f"{user.get('id')}"] = task_list
    with open("todo_all_employees.json", mode="w") as file:
        json.dump(all_users_dict, file)
