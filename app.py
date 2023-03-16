from flask import Flask, render_template, request, flash

app = Flask(__name__)

app.secret_key = "KEY-89131789371";

@app.route('/hello')
def index():
    flash('Hello World!')
    return render_template('index.html')


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    name = str(request.form['name_input'])
    flash('Hello'+name)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
