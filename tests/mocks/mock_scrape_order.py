from bson import ObjectId

scrape_order_id = "62ffee8d70f768217a498f89"
scrape_order_id_completed = "62ffee8d70f768217a498f89"
scrape_order_id_not_completed = "62ffeda070f768217a498f71"


def mock_scrape_order(self):
    return "62ffee8d70f768217a498f89"


def mock_scrape_order_not_completed(self, order_id):
    return {
        "_id": ObjectId("62ffeda070f768217a498f71"),
        "start": "2022-08-19T20:08:00.095Z",
        "end": None,
    }


def mock_scrape_order_completed(self, order_id):
    return {
        "id": "62ffee8d70f768217a498f89",
        "start": "2022-08-19T20:11:57.893Z",
        "end": "2022-08-19T20:12:27.882Z",
    }
