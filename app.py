from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MongoDB Atlas URI
app.config["MONGO_URI"] = "mongodb+srv://myuser:CWEf0LIJiDt6M0kf@clustersg.6jrur.mongodb.net/mydatabase?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form data
        name = request.form['name']
        age = request.form['age']

        # Insert data into MongoDB
        mongo.db.students.insert_one({'name': name, 'age': age})

        # Redirect to success page
        return redirect(url_for('success'))

    except Exception as e:
        flash(f"Error: {str(e)}", 'error')
        return render_template('index.html')

@app.route('/success')
def success():
    return "Data submitted successfully"

if __name__ == '__main__':
    app.run(debug=True)