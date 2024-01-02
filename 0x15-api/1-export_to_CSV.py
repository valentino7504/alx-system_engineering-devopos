#!/usr/bin/python3
'''
This module is used to extract API responses and
export them to a CSV`
'''
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
    with open(file=f"{employee_id}.csv", mode="w") as file:
        for task in todos:
            file.write(f'"{employee_id}","{username}",' +
                       f'"{task.get("completed")}","{task.get("title")}"\n')
