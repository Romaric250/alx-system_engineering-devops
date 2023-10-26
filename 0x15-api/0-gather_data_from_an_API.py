#!/usr/bin/python3
"""Accessing a REST API for employess"""

import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    base_Url = "https://jsonplaceholder.typicode.com/users"
    url = baseU_rl + "/" + employee_Id

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

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for task in done_task:
        print("\t {}".format(task.get('title')))
