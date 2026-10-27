import csv

def load_logins(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)

        login_list = []
        for login in reader:
            login_list.append(login)

    return login_list