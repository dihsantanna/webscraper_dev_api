app_install:
	pip install -e .["dev"]

install:requirements.txt
	pip install -r requirements.txt

compose-up:
	docker-compose up -d --build

compose-down:
	docker-compose down --remove-orphans

api-run:
	python -m flask run --host=0.0.0.0

scraper-run:
	python ./src/scrape.py