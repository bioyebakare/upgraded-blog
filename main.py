from flask import Flask, render_template
import requests

BLOG_URL = "https://api.npoint.io/159df8cf34fc36e1ad92"
response = requests.get(BLOG_URL)
blog_posts = response.json()
print(blog_posts[0])

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=blog_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/blog/<int:post_id>")
def single_blog(post_id):
    return render_template("post.html", posts=blog_posts, post_id = post_id)

if __name__ == "__main__":
    app.run(debug=True)