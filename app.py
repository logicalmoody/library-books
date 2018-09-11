from flask import Flask, render_template, request
from scraper import scrape
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		# update review
		x = request.form['barcode']
		scrape(x)

	return render_template('header.html')


if __name__ == '__main__':
    app.run()
