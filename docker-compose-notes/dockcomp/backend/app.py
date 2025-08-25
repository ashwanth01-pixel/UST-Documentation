from flask import Flask, jsonify
app = Flask(__name__)
counter = 0

@app.route('/increment')
def increment():
    global counter
    counter += 1
    return jsonify(count=counter)

@app.route('/decrement')
def decrement():
    global counter
    counter -= 1
    return jsonify(count=counter)

@app.route('/')
def get():
    return jsonify(count=counter)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
