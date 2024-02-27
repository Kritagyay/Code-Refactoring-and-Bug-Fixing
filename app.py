from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Create an empty list to store the notes
notes = []

# Define the route for the index page
# Allow both GET and POST methods for this route
# In the previous code, only POST method was allowed which was incorrect
@app.route('/', methods=["GET", "POST"])
def index():
    # Check if the request method is POST
    if request.method == "POST":
        # Get the note from the form data
        # In the previous code, request.args.get("note") was used
        # But request.args is used to get parameters from the query string of a GET request
        # Since we're sending the form data with a POST request, we should use request.form.get("note") instead
        note = request.form.get("note")
        # Check if the note is not empty
        # This check was missing in the previous code
        # Without this check, empty notes would be added to the list
        if note:
            # Append the note to the notes list
            notes.append(note)
    # Render the home.html template
    # Pass the notes list to the template
    return render_template("home.html", notes=notes)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
