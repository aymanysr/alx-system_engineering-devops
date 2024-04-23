#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
from a REST API.
It takes an employee ID as an argument and displays their TODO list progress
in a specific format.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"

    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    parameters = {"userId": employee_id}

    todo_url = f"{base_url}/todos/"
    todo_response = requests.get(todo_url, params=parameters)
    todo_data = todo_response.json()

    completed = []

    for todo in todo_data:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    print(f"Employee {user_data.get('name')} is done with tasks"
          f"({len(completed)}/{len(todo_data)}):")

    for complete in completed:
        print("\t {}".format(complete))
