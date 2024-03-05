from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # This function returns a simple string
    return 'Hello World from Aidan Powers! I am adding my first code change.'


@app.route('/hello')
def hello():  # This route renders the 'hello.html' template
    return render_template('hello.html')


@app.route('/about')
def about():  # This route renders the 'about.html' template
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')



if __name__ == '__main__':
    app.run()
