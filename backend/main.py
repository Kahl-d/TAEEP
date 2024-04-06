from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test')
def main():
    return jsonify({'message': 'Hello from the backend!'})

if __name__ == '__main__':
    app.run()