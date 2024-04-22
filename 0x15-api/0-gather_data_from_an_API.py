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

    # Fetch employee data
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    if user_response.status_code != 200 or todo_response.status_code != 200:
        print("Failed to retrieve data")
        sys.exit(1)

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data["name"]
    all_tasks = len(todo_data)

    completed_tasks = [task for task in todo_data if task["completed"]]
    completed_count = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with tasks"
        f"({completed_count}/{all_tasks}):"
    )

    for task in completed_tasks:
        print(f"\t {task['title']}")
