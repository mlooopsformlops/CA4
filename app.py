# app.py

from flask import Flask, render_template, request, redirect
import pymongo
import os

app = Flask(__name__)

def connect_to_mongodb():
    # Retrieve MongoDB credentials from environment variables
    username = os.environ.get("MONGO_USERNAME")
    password = os.environ.get("MONGO_PASSWORD")
    
    # Connect to MongoDB with authentication
    client = pymongo.MongoClient(f"mongodb://{username}:{password}@mongodb:27017/")
    return client

def get_collection(database_name, collection_name):
    client = connect_to_mongodb()
    # Select database
    db = client[database_name]

    # Select collection
    collection = db[collection_name]
    return collection

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']

        # Store data in MongoDB
        database_name = "mlops_database"  # Database name
        collection_name = "mlops_collection"  # Collection name
        collection = get_collection(database_name, collection_name)
        collection.insert_one({'name': name, 'subject': subject})
        
        return redirect('/')
    else:
        # Retrieve data from MongoDB
        database_name = "mlops_database"  # Database name
        collection_name = "mlops_collection"  # Collection name
        collection = get_collection(database_name, collection_name)
        documents = list(collection.find())
        
        return render_template('index.html', documents=documents)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')