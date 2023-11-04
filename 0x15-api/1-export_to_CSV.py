#!/usr/bin/python3
"""Accessing a REST API for todoloyees"""

import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    base_Url = "https://jsonplaceholder.typicode.com/users"
    url = base_Url + "/" + employee_Id

    res = requests.get(url)
    username = res.json().get('username')

    todo_Url = url + "/todos"

    res = requests.get(todo_Url)

    tasks = res.json()

    with open('{}.csv'.format(employee_Id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_Id, username, task.get('completed'),
                               task.get('title')))
