import requests
from flask import Flask, render_template_string

app = Flask(__name__)
BACKEND_URL = "http://backend:5000"

TEMPLATE = """
<h2>Counter: {{ count }}</h2>
<a href="/inc"><button>Increment</button></a>
<a href="/dec"><button>Decrement</button></a>
"""

@app.route('/')
def index():
    r = requests.get(BACKEND_URL)
    return render_template_string(TEMPLATE, count=r.json()["count"])

@app.route('/inc')
def inc():
    requests.get(BACKEND_URL + "/increment")
    return index()

@app.route('/dec')
def dec():
    requests.get(BACKEND_URL + "/decrement")
    return index()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
