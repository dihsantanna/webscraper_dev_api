import json

PATH = "src/data/notebooks_infos.json"


def save_in_json(infos):
    with open(file=PATH, mode="w") as file:
        json.dump(infos, file)


def load_from_json():
    try:
        with open(file=PATH, mode="r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None
