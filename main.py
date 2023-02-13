from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def load_page():
    #data = 'hello'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8080, threaded=1)