#!/usr/bin/python3
"""export to CSV"""
from sys import argv
import csv
import requests


def main():
    """main function"""
    BASE_URL = 'https://jsonplaceholder.typicode.com/'
    id_user = argv[1]
    user = requests.get(f'{BASE_URL}users/{id_user}').json()
    todos = requests.get(f'{BASE_URL}/users/{id_user}/todos').json()
    with open(f'{id_user}.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos:
            if task.get('userId') == int(id_user):
                writer.writerow([id_user, user.get('name'),
                                task.get('completed'), task.get('title')])


if __name__ == "__main__":
    main()
