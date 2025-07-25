from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import csv
app = Flask(__name__)
print(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        name = data['name']
        email = data['email']
        message = data['message']
        print(f'{name}, {email}, {message}')
        with open("database.csv", "a", encoding='utf-8') as file:
            file.write(str(f'{name}, {email}, {message}') + "\n")
        return redirect(url_for('response', success=True))
    # return render_template("index.html", success=True)

    else:
        return "something is wrong"
@app.route('/response')
def response():
    return "<p>I will get back to you as soon as possible<p>"

if __name__ == '__main__':
    app.run(debug=True)
