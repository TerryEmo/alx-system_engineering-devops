#!/usr/bin/python3
"""
Export data in the CSV format.
For a given employee ID,
records all tasks that are owned by this employee.
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
API: https://jsonplaceholder.typicode.com/users/1/todos
"""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/users/'
    userId = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId))
    name = user.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    filename = userId + '.csv'
    with open(filename, mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if task.get('userId') == int(userId):
                writer.writerow([userId, name, str(task.get('completed')),
                                 task.get('title')])
