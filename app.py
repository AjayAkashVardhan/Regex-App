from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex']
    matches = re.findall(regex_pattern, test_string)
    return render_template('results.html', matches=matches,test_string=test_string)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    # Regular expression for email validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    is_valid_email = re.match(email_regex, email) is not None
    return render_template('email_validation_result.html', is_valid_email=is_valid_email,email=email)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')