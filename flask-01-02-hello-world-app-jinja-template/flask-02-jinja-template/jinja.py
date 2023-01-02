from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def head():
      return render_template("index.html", number1=250, number2=500)

@app.route("/mult")

def number():
      x=10
      y=20
      return render_template("body.html", num1=x, num2=y, mult=x*y)


if __name__ == "__main__":
      app.run(port=3000, debug=True)