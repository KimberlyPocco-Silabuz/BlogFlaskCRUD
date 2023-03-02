from flask import Blueprint, render_template, redirect, request, session
from flask_login import LoginManager,logout_user,login_required,current_user, login_user
from app.db import db
from datetime import datetime
from werkzeug.urls import url_parse

app_router = Blueprint("app_router", __name__)

@app_router.route("/")
def index():
    return render_template("index.html")
