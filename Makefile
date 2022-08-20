freeze:
	pip freeze > requirements.txt

lint:
	flake8 ./webscraper_api/

install:requirements.txt
	pip install -r requirements.txt

compose-up:
	docker-compose up -d --build

compose-down:
	docker-compose down --remove-orphans

dev:
	python ./webscraper_api/server.py

start:
	python -m flask run --host=0.0.0.0

scraper-run:
	python scrape_init.py