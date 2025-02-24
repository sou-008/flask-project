from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# MongoDB Configuration (use the MONGO_URI from .env file)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")  # Fetches the URI from environment variables
mongo = PyMongo(app)

# Route to handle To-Do submission
@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    # Get data from the POST request (Item Name and Item Description)
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    if item_name and item_description:
        todo_item = {
            'item_name': item_name,
            'item_description': item_description
        }
        # Insert the To-Do item into the MongoDB collection
        mongo.db.todo_items.insert_one(todo_item)
        return jsonify({'message': 'To-Do item added successfully!'}), 201
    
    # If either field is missing
    return jsonify({'message': 'Item name and description are required.'}), 400

if __name__ == '__main__':
    app.run(debug=True)