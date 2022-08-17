import json


def save_in_json(infos, path):
    with open(path, mode="w") as file:
        json.dump(infos, file)


def load_from_json(path):
    try:
        with open(path, mode="r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None
