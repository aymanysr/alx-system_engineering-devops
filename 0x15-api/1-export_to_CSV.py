#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to a CSV file.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then writes the tasks owned by the employee into a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]

    BASE_URL = "https://jsonplaceholder.typicode.com"

    users_url = f"{BASE_URL}/users/{user_id}"
    user_response = requests.get(users_url)
    users_data = user_response.json()

    username = users_data.get("username")

    parameters = {"userId": user_id}

    todos_url = f"{BASE_URL}/todos/"
    todo_response = requests.get(todos_url, params=parameters)
    todos_data = todo_response.json()

    with open(f"{user_id}.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo in todos_data:
            writer.writerow([user_id, username, todo.get("completed"),
                             todo.get("title")])
