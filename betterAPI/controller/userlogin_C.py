from app import app
from model.userlogin_M import *
from flask import request

obj = userlogin_M(); 

@app.route('/userlogin/get')
def userlogin():
    print("User Login Controller Accessed")
    return obj.userlogin_model(); 


@app.route('/userlogin/post', methods=['POST'])
def userlogin_post():
    print("user login post controller is running successfully")
    return obj.userlogin_post_model(request.form); 


@app.route('/userlogin/put', methods=['PUT'])
def userlogin_put():
    print("user login put controller is running successfully")
    return obj.userlogin_put_model(request.form); 


@app.route('/userlogin/delete/<id>', methods = ['DELETE'])
def userlogin_delete(id):
    print("user login delete controller is running successfully")
    return obj.userlogin_delete_model(id);