from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define the root route
@app.route("/")
def hello_world():
    return "hello mitron"

# Run the local development server
if __name__ == "__main__":
    app.run(debug=True)