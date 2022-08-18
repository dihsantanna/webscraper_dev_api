from http import HTTPStatus as status

from scraper.helpers.json_handler import load_from_json

GET_NOTE_ERROR_MSG = "Robot starting up. Wait some minutes and try again."


def get_notebooks():
    try:
        data = load_from_json()
        if not data:
            return {"message": GET_NOTE_ERROR_MSG}, status.NOT_FOUND
        return data, status.OK
    except Exception:
        return (
            {"message": "Internal server error"},
            status.INTERNAL_SERVER_ERROR,
        )
