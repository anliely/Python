from . import main
from ..models import *
from flask import render_template

@main.route("/index")
@main.route('/')
def index():
    return render_template("index.html")

@main.route("/blog")
def blog_views():
    return render_template("blog.html")

@main.route("/about")
def about_views():
    return render_template("about.html")

@main.route("/contact")
def contact_veiws():
    return render_template("contact.html")

@main.route("/server")
def server_views():
    return render_template("server.html")


