from flask import render_template, request, Blueprint
from flask import Blueprint

main = Blueprint("main", __name__)

#  Route decorators
@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")
