from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app = Flask(__name__)
CORS(app)
client = MongoClient('mongodb://localhost:27017/')
db = client['rtsp-livestream']
overlays = db['overlays']
@cross_origin()

@app.route('/stream', methods=['GET'])
def get_stream():
    stream_url = 'https://www.youtube.com/watch?v=1k8H2CywVqg'
    return jsonify({ 'url': stream_url }), 200

@app.route('/overlay', methods=['POST'])
def create_overlay():
    content = request.json['content']
    overlay = { 'content': content }
    overlays.insert_one(overlay)
    return jsonify({ 'message': 'Overlay created successfully' }), 201

@app.route('/overlay/<id>', methods=['DELETE'])
def delete_overlay(id):
    overlays.delete_one({ '_id': ObjectId(id) })
    return jsonify({ 'message': 'Overlay deleted successfully' }), 200

@app.route('/home', methods=['GET'])
def home():
    print("hello")

if __name__ == '__main__':
    app.run(debug=True)