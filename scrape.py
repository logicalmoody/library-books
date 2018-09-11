'''
Contributors: Calvin Moody, mcuddy77

REQUIRED PACKAGES (from pip or other python package manager):
	bs4
	requests

TODO:	[ ] Make the program wait for barcode input from the pi
		[ ] Make the program take a variable and store it in barcode
		[ ] Take the picture link and put it into the html file, rendered as a link.
		[ ] Format the HTML with a CSS file to make it nice for the reader.
		[ ] Display the HTML in the pi's native browser (preferably in some kind of kiosk mode)
		[ ] Make the program wait for a specified amount of time before closing the browser (or routing back to the welcome screen)
		[ ] Handle errors?


TESTING BARCODES:
	- R0015650030
	- R2004251910
	- R2004758583
'''

# Importing libraries for use in the project
from __future__ import print_function
from bs4 import BeautifulSoup
import requests

prev_barcode = ""
barcode = ""

while True:
	print("Enter a barcode: ", end="")
	# Set to barcode of book to search for (will be retrieved from scanner eventually)
	# barcode = "R2004758583" #raw_input()
	# print(read())
	# barcode = read()
	# barcode = tuple(barcode)[1]
	# barcode = barcode.strip()
	# print(barcode)
	barcode = input()

	if barcode != prev_barcode:
		# Do we need separate urls for the different kinds of bar codes? See 20004003485 above.
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

		# Write the HTML!
		print("Generating HTML file... ", end="")
		f = open("./templates/review.html", "w")

		f.write("<input type='text' autofocus />")

		# Write the book title here

		# Write the reviews
		for rev in review_list:
			f.write(rev)
			f.write("<br/>")

		f.close()
		print("done")
	else:
		print("Same barcode detected")

	prev_barcode = barcode
