from api.app import scraper, app

if __name__ == "__main__":
    scraper.scrape()
    app.run(debug=True, port=5000)
