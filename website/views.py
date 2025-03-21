from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
import requests
import os

views = Blueprint('views', _name_)

@views.route('/')
#login required eklenebilir
def home():
    return render_template("base.html")
    #anasayfa.html eklenebilir

@views.route('/anasayfa')
@login_required
def mainPage():
    return render_template("anasayfa.html", user=current_user)