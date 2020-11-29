from flask import Flask, render_template, url_for, flash
from forms import RegistrationForm, LoginForm
import save_data as sd
app = Flask(__name__)

app.config['SECRET_KEY'] = '6e10fe750c13a1e1220a9cc63307664c'

courses_list = sd.get_courses_json()

@app.route("/")
@app.route("/courses")
def courses():
    return render_template('courses.html', courses_list=courses_list)

@app.route("/assignments")
def assignments():
    return render_template('assignments.html')

if __name__ == '__main__':
    app.run(debug=True)
