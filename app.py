from flask import Flask

app = Flask(__name__)


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


if __name__ == '__main__':
    app.run()
