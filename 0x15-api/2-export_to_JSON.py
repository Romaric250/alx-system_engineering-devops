#!/usr/bin/python3
"""Accessing a REST API for employees"""

import requests
import sys
import json

if __name__ == '__main__':
    employee_Id = sys.argv[1]
    base_Url = "https://jsonplaceholder.typicode.com/users"
    url = base_Url + "/" + employee_Id

    response = requests.get(url)
    employeeName = response.json().get('name')

    todo_Url = url + "/todos"

    response = requests.get(todo_Url)

    tasks = response.json()

    done = 0
    done_task = []

    for task in tasks:
        if task.get('completed'):
            done_task.append(task)
            done += 1

    json_filename = "{}.json".format(employee_Id)

    data = {
        "USER_ID": employee_Id,
        "USERNAME": employeeName,
        "tasks": []
    }

    for task in done_task:
        data["tasks"].append({
            "TASK_COMPLETED_STATUS": "True",
            "TASK_TITLE": task.get('title')
        })

    for task in tasks:
        if not task.get('completed'):
            data["tasks"].append({
                "TASK_COMPLETED_STATUS": "False",
                "TASK_TITLE": task.get('title')
            })

    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print("Data exported to {} successfully.".format(json_filename))
