import sys
from flask import Flask
app = Flask(__name__)

@app.route("/")
def basic():
  name = sys.argv[1]
  print("Hello " + name + "!")
