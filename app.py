from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to store bookmarks
bookmarks = []

# Route to display bookmarks on the index page
@app.route("/")
def index():
    return render_template("index.html", bookmarks=bookmarks)

# Route to add a new bookmark
@app.route("/add_bookmark", methods=["POST"])
def add_bookmark():
    # Get the title and URL from the form
    title = request.form.get("title")
    url = request.form.get("url")
    
    # Check if both title and URL are provided
    if title and url:
        # Create a new bookmark dictionary
        bookmark = {"id": len(bookmarks) + 1, "title": title, "url": url}
        # Add the new bookmark to the list
        bookmarks.append(bookmark)

    # Redirect to the index page after adding a bookmark
    return redirect(url_for("index"))

# Route to delete a bookmark based on its ID
@app.route("/delete_bookmark/<int:bookmark_id>")
def delete_bookmark(bookmark_id):
    global bookmarks
    # Create a new list without the specified bookmark ID
    bookmarks = [bookmark for bookmark in bookmarks if bookmark["id"] != bookmark_id]
    # Redirect to the index page after deleting a bookmark
    return redirect(url_for("index"))

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
