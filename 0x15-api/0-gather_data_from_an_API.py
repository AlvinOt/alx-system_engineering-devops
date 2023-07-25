#!/usr/bin/python3
"""
This is a pyhton script that uses
this REST API < https://jsonplaceholder.typicode.com/ >,
to return information about employee ID TODO list progress.
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    call_employee = requests.get(url + "users/{}".format(user_id)).json()
    call_todos = requests.get(url + "users/{}/todos".format(user_id)).json()
    completed = []
    for task in call_todos:
        if task["completed"] is True:
            completed.append(task)
    print("Employee {} is done with tasks({}/{}):"
          .format(call_employee["name"], len(completed), len(call_todos)))
    for task in completed:
        print("\t", task["title"])
