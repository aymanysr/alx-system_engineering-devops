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

    # Check if the employee ID is provided
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    # Base URL for the JSONPlaceholder API
    BASE_URL = "https://jsonplaceholder.typicode.com/"

    # Get the users information
    users_url = f"{BASE_URL}users/{user_id}"
    user_response = requests.get(users_url)
    users_data = user_response.json()

    username = users_data.get("username")

    parameters = {"userId": user_id}

    # Get the to-do list for the user
    todos_url = f"{BASE_URL}todos/"
    todo_response = requests.get(todos_url, params=parameters)
    todos_data = todo_response.json()

    # Construct the CSV file name using the employee ID
    csv_file_name = f"{user_id}.csv"

    # Open the CSV file and write the data
    with open(csv_file_name, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Write each todo to the CSV file
        for todo in todos_data:
            writer.writerow([
                user_id,
                users_data.get("name"),
                todo.get("completed"),
                todo.get("title"),
            ])

    print(f"Data exported to {csv_file_name}")
