# Flask Project
This repository contains a Flask-based project that implements two applications: one for submitting student data to MongoDB, and another for interacting with data stored in a backend file and inserting To-Do items into MongoDB.

## Folder Structure

/flask-project
<br>│
<br>├── app.py                # Main Flask application for student data submission
<br>├── app1.py               # Flask application to serve the /api route with data from the backend file
<br>├── app2.py               # Flask application for To-Do item submission to MongoDB
<br>├── requirements.txt      # List of required Python packages for the project
<br>├── templates/            # Folder containing the HTML templates
<br>│   ├── index.html        # HTML form to submit student data
<br>│   └── todo.html         # HTML form to submit To-Do items
<br>├── .gitignore            # Git ignore file to exclude unnecessary files
<br>└── README.md             # Project readme


## Setup and Installation
### Prerequisites
- Install Python (version 3.6 or later) from here.
- Install MongoDB Atlas and set up a free-tier cluster.
- Obtain the MongoDB URI from your Atlas dashboard and save it as an environment variable (or use a .env file to store it securely).

### Step 1: Clone the Repository
<br>Clone the repository to your local machine using the following command:
<br>git clone https://github.com/your-username/git-repositoty-name.git
<br>cd git-repository-name

### Step 2: Install Dependencies
<br>Install the required Python dependencies by running:
<br>pip install -r requirements.txt

### Step 3: Set Up Environment Variables
<br>Create a .env file in the root of the project and add the following:
<br>MONGO_URI=<your-mongodb-atlas-uri>

**Make sure to replace <your-mongodb-atlas-uri> with your actual MongoDB URI.**

### Step 4: Run the Applications
<br>To run the Flask applications, you need to run each file separately:

1. For the student data submission application (app.py):
<br>python app.py

2. For the data API (serving backend file data) (app1.py):
<br> python app1.py

3. For the To-Do item submission application (app2.py):
<br>ython app2.py

### Each application will be available at the following URLs:

- app.py will be running on http://localhost:5000/
- app1.py will be running on http://localhost:5000/api
- app2.py will be running on http://localhost:5000/success

### Features

`app.py` - Student Data Submission Application
- This application accepts student data (name and age) through a form.
- The form data is inserted into MongoDB.
- Upon successful submission, the user is redirected to a success page.

`app1.py` - Data API
-This application exposes an /api route that serves a JSON response.
-The response is read from a backend file (data.json).
-If an error occurs while reading the data, it returns an error message.

`app2.py` - To-Do Item Submission
- This application accepts To-Do item data (name and description) through a form.
- The data is inserted into MongoDB.
- Returns a success or error message based on the submission status.

### How to Use

- Open http://localhost:5000/ in your browser to access the student data submission form.
- Submit student information (name and age), which will be stored in your MongoDB database.
- Access http://localhost:5000/api to see the data served from the backend file in JSON format.
- Use http://localhost:5000/success to submit To-Do items, which will be saved to MongoDB.

### Troubleshooting
- Ensure your MongoDB Atlas URI is correctly configured in the .env file.
- Make sure the necessary environment variables are loaded (you can use python-dotenv for automatic loading).
- Check that MongoDB Atlas allows connections from your current IP address.
- If you face any issues with dependencies, make sure to install the required libraries using the requirements.txt file.

### Clean Up
To remove the MongoDB data or resources:

- Delete entries manually from MongoDB Atlas if required.
- Delete the project folder if you no longer need the application.