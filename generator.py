def generate():
	"""# Write the HTML!
	print("Generating HTML file... ", end="")
	f = open("./templates/review.html", "w")

	# Write the book title here
	f.write(str(title))
	f.write(author)
	f.write("<h3>Subjects:</h3>")
	f.write("<ul>")
	for t in types:
		f.write("<li>")
		f.write(t.text)
		f.write("</li>")
	f.write("</ul>")
	# Write the picture here
	f.write(picture_link)

	# Write the reviews
	for rev in review_list:
		f.write(rev)
		f.write("<br/>")

	f.close()
	print("done")"""