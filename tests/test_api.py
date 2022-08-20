import json
from unittest.mock import patch

from flask import Flask
from flask.testing import FlaskClient
from flask_pymongo import PyMongo
from webscraper_api.api.app import create_app

from .mocks.mock_notebooks import find_notebooks_mock, notebooks
from .mocks.mock_scrape_order import (
    mock_scrape_order,
    mock_scrape_order_completed,
    mock_scrape_order_not_completed,
    scrape_order_id,
    scrape_order_id_completed,
    scrape_order_id_not_completed,
)


def test_create_app_returns_flask_instance(client_test: FlaskClient):
    """Tests if Flask has been installed correctly."""
    app = create_app()
    assert type(app) == Flask


def test_get_notebooks(client_test: FlaskClient):
    """Tests if GET method returns notebooks."""
    with patch(
        "webscraper_api.api.services.notebook.NotebookService.get_all_notebooks",
        find_notebooks_mock,
    ):
        response = client_test.get("/notebooks")

        assert response.status_code == 200
        assert json.loads(response.data) == notebooks


def test_post_scrape_order(client_test: FlaskClient):
    """Checks if it is possible to add a scrape order, and the return is as expected."""
    with patch(
        "webscraper_api.api.services.scrape.ScrapeService.post_scrape_order", mock_scrape_order
    ):
        response = client_test.post("/scrape")

        assert response.status_code == 201
        assert json.loads(response.data) == {
            "message": "Scrape order created!",
            "order_id": scrape_order_id,
        }


def test_get_scrape_order_not_completed(client_test: FlaskClient):
    """
    Checks if by passing the orderId as a query,
    it is possible to check the scraping progress.
    In this case the scraping must NOT have been completed.
    """
    with patch(
        "webscraper_api.api.services.scrape.ScrapeService.get_scrape_order_by_id",
        mock_scrape_order_not_completed,
    ):
        response = client_test.get(f"/scrape?orderId={scrape_order_id_not_completed}")

        assert response.status_code == 200
        assert json.loads(response.data) == {"message": "Scraping order is not completed"}


def test_get_scrape_order_completed(client_test: FlaskClient):
    """
    Checks if passing the orderId as a query,
    you can check the scraping progress.
    In this case, the scraping must have been COMPLETED.
    """
    with patch(
        "webscraper_api.api.services.scrape.ScrapeService.get_scrape_order_by_id",
        mock_scrape_order_completed,
    ):
        response = client_test.get(f"/scrape?orderId={scrape_order_id_completed}")

        assert response.status_code == 200
        assert json.loads(response.data) == {"message": "Scraping order already completed"}


def test_get_scrape_order_nonexistent(client_test: FlaskClient):
    """
    Checks if passing a non-existent orderId with query in a request.
    You must return the message: 'Scraping order does not exist'
    """
    with patch(
        "webscraper_api.api.services.scrape.ScrapeService.get_scrape_order_by_id",
        lambda self, order_id: None,
    ):
        response = client_test.get("/scrape?orderId=invalid_order_id")

        assert response.status_code == 404
        assert json.loads(response.data) == {"message": "Scraping order does not exist"}
