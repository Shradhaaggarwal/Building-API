from app import app
from model.userlogin_M import *

obj = userlogin_M(); 

@app.route('/userlogin')
def userlogin():
    print("User Login Controller Accessed")
    return obj.userlogin_model(); 
