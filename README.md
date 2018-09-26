# library-books

## Technology Stack

- Flask
- Python 3
- Pipenv

## Overview

This application runs on a Raspberry Pi and uses a barcode scanner to get a book's ISBN number, scrape the Atlanta Fulton Public Library's [website](https://afpl.ent.sirsi.net/client/en_US/default/search/results) to pull reviews and other data about the book, and then renders a webpage to display it.

The Pi will display on some kind of TV screen. Because there is no mouse/keyboard input, the webpage should display entirely on the screen without needing to scroll. The reviews should appear in an auto-sliding carousel.

### Directory

```
app.py # runs the Flask server and calls the scraper with the barcode number
scraper.py # scrapes the book data and passes a dictionary of the book data to generator
generator.py # structures the scraped data into HTML and writes to the review.html file
templates/
          header.html # base html file. put any refs to CSS and JS here
          review.html # this file is generated and ignored by git
```

## Getting Started

Make sure you have both Python 3 and pipenv installed.

Run the following commands to get the local server running on [localhost:5000](http://localhost:5000/)

- $ `pipenv shell`
- $ `pipenv install`
- $ `python3 app.py`

### Notes

To install `pipenv` on macOS:
Install [Homebrew](https://brew.sh/) and run `brew install pipenv`
