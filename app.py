from flask import Flask, render_template  # to use template

app = Flask(__name__)


@app.route('/')  # route--> part of url after the domain name
def hello_world():
  #return "Hello, world"
  return render_template('home.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  # local host
