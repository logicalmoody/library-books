# Importing libraries for use in the project
from __future__ import print_function
from generator import generate
from bs4 import BeautifulSoup
import requests


def scrape(barcode):
	request = "http://afpl.ent.sirsi.net/client/en_US/default/search/results?qu=" + barcode + "#tabs-4"

	# Scrape the reviews from the DOM
	print("Scraping reviews... ", end="")
	response = requests.get(request)
	soup = BeautifulSoup(response.text, "html.parser")
	target_divs = soup.find_all("div", {"class": "enrichedContentElement"})

	'''
	# Scrape the picture from the DOM
	picture_link = soup.find("img", {"id": "detailCover0"})
	# removing garbage from the image link (might not be consistent)
	picture_link = str(picture_link).replace("amp;", "")
	# print(picture_link)
	'''

	# Get the reviews
	review_list = []
	for div in target_divs:
		# Only get items with "Review" in the header
		if "Review</h3>" in str(div):
			review_list.append(str(div))
	print("done")

	# Scrape the title from the DOM
	title = soup.find("div", {"class": "displayElementText INITIAL_TITLE_SRCH"}).text
	# Scrape the picture from the DOM
	image = soup.find("img", {"id": "detailCover0"})
	# removing garbage from the image link (might not be consistent)
	image = str(image).replace("amp;", "")

	# Scrape the author
	author = soup.find("div", {"class": "displayElementText INITIAL_AUTHOR_SRCH"}).text
	author = author.text
	author = author.replace(", author.", "")
	author = author.replace(" author.", "")

	# Scrape the types
	types = soup.find_all("div", {"class": "displayElementText SUBJECT_TERM"})

	# Create JSON to pass to generator
	data = {
		"title": title,
		"author": author,
		"image": image,
		""
	}

	# Call generator
	generate()


