from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api')
def api():
    try:
        # Read data from the backend file
        with open('data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)