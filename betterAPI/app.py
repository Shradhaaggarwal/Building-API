from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Better API!"

# import betterAPI.controller.userlogin as userlogin
# from controller import userlogin,usersignup 

from controller import *