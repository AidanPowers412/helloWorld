from flask import Flask, render_template, request

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

@app.route('/favorite-course')
def favorite_course():
    subject = request.args.get('subject', 'No Subject')
    course_number = request.args.get('course_number', 'No Course Number')
    return render_template('favorite-course.html', subject=subject, course_number=course_number)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        emailAddress = request.form.get('emailAddress')
        age = request.form.get('age')
        return render_template('contact.html', submitted=True, firstName=firstName, lastName=lastName, emailAddress=emailAddress, age=age)
    else:
        return render_template('contact.html', submitted=False)




if __name__ == '__main__':
    app.run()
