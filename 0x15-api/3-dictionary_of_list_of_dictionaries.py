import json
import requests
import sys


if __name__ == '__main__':
    users_url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(users_url)
    users = response.json()

    tasks_dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
        response = requests.get(todos_url)
        tasks = response.json()
        tasks_dictionary[user_id] = []
        for task in tasks:
            tasks_dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(tasks_dictionary, file)
