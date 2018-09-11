from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('review.html')


# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()