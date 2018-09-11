# Importing libraries for use in the project
from __future__ import print_function
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
	title = soup.find("div", {"class": "displayElementText INITIAL_TITLE_SRCH"})
	# Scrape the picture from the DOM
	picture_link = soup.find("img", {"id": "detailCover0"})
	# removing garbage from the image link (might not be consistent)
	picture_link = str(picture_link).replace("amp;", "")

	# Write the HTML!
	print("Generating HTML file... ", end="")
	f = open("./templates/review.html", "w")

	# Write the book title here
	f.write(str(title))
	# Write the picture here
	f.write(picture_link)

	# Write the reviews
	for rev in review_list:
		f.write(rev)
		f.write("<br/>")

	f.close()
	print("done")
