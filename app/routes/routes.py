from flask import Blueprint, render_template, redirect, request, session
from app.db import db
from datetime import datetime

app_router = Blueprint("app_router", __name__)