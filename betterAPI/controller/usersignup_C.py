from app import app
from model.usersignup_M import *

obj = usersignup_M(); 

@app.route('/usersignup')
def usersignup():
    print("User Signup Controller Accessed")
    return obj.usersignup_model(); 