from flask import Flask, render_template
from pymongo import MongoClient
import os

app = Flask(__name__)
MONGO_USER = os.getenv('ROOT_USERNAME')
MONGO_PASSWORD = os.getenv('ROOT_PASSWORD')

# Update the MongoDB URI to match your MongoDB container configuration
client = MongoClient(f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@mongo:27017/')
db = client['testdb']  # Assuming you have a database named 'testdb'

@app.route('/hello')
def hello():
    return "hello world"

@app.route('/', methods=["GET"])
def show_collections():
    collections = db.list_collection_names()  # List all collection names in the database
    return render_template('index.html', collections=collections)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
