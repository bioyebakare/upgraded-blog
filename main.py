from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

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

def do_the_login():
    name = request.form.get("name")
    email = request.form.get("email")
    no = request.form.get("phone")
    msg = request.form.get("message")
    print(name)
    print(email)
    print(no)
    print(msg)
    x = f"Name: {name}\nEmail: {email}\nPhone: {no}\nMessage: {msg}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=os.getenv("MY_EMAIL"), password=os.getenv("MY_PASSWORD"))
        connection.sendmail(from_addr=os.getenv("MY_EMAIL"), to_addrs="bioyebak@gmail.com", msg=f"Subject: You have 1 message from your Blog📩\n\n{x}".encode("utf-8"))
    return render_template('contact.html', msg_sent=True)

def show_the_log_in_form():
    return render_template("contact.html", msg_sent=False)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return do_the_login()
    else:
        return show_the_log_in_form()

@app.route("/blog/<int:post_id>")
def single_blog(post_id):
    return render_template("post.html", posts=blog_posts, post_id = post_id)




if __name__ == "__main__":
    app.run(debug=True)