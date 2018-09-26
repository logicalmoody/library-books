def generate(data):
	# Write the HTML!
	print("Generating HTML file... ", end="")
	f = open("./templates/review.html", "w")

	# Write the book title here
	f.write(data['title'])
	f.write(data['author'])
	f.write("<h3>Subjects:</h3>")
	f.write("<ul>")
	for t in data['genres']:
		f.write("<li>")
		f.write(t)
		f.write("</li>")
	f.write("</ul>")
	# Write the picture here
	f.write(data['image_link'])

	# Write the reviews
	for rev in data['reviews']:
		f.write(rev)
		f.write("<br/>")

	f.close()
	print("done")