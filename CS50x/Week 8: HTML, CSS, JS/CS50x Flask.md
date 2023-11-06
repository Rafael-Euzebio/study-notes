# Flask
Flask is a [[ST Web Framework]] for [[CS50x Python]]. It has minimal components and does not requires any specific libraries, for that reason it is considered a **microframework**

## Components
One of its components is the template engine [[CS50x Jinja]]

## Usage
```py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
```
