# Flask
Flask is a [Web Framework](ST_Web-Framework) for [Python](../Week-6_Python/CS50x_Python.md). It has minimal components and does not requires any specific libraries, for that reason it is considered a **microframework**

## Components
One of its components is the template engine [Jinja](./CS50x_Jinja.md)

## Usage
```py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
```