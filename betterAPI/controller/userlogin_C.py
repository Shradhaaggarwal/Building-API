from app import app
from model.userlogin_M import *
from model.user_auth import *
from flask import request

obj = userlogin_M(); 
objauth = userAuth_M(); 

@app.route('/userlogin/get')
@objauth.token_auth_model()
def userlogin():
    print("User Login Controller Accessed")
    return obj.userlogin_model(); 


@app.route('/userlogin/post', methods=['POST'])
@objauth.token_auth_model()
def userlogin_post():
    print("user login post controller is running successfully")
    return obj.userlogin_post_model(request.form); 


@app.route('/userlogin/put', methods=['PUT'])
@objauth.token_auth_model()
def userlogin_put():
    print("user login put controller is running successfully")
    return obj.userlogin_put_model(request.form); 


@app.route('/userlogin/delete/<id>', methods = ['DELETE'])
@objauth.token_auth_model()
def userlogin_delete(id):
    print("user login delete controller is running successfully")
    return obj.userlogin_delete_model(id); 


@app.route('/userlogin/patch/<id>', methods= ['PATCH'])
def userlogin_patch(id):
    print("user login patch controller is running successfully")
    return obj.userlogin_patch_model(request.form, id)

@app.route('/userlogin/get/limit/<limit>/pageno/<pgno>')
def userlogin_pagination(limit, pgno):
    print("User Login Pagination Controller Accessed")
    return obj.userlogin_pagination_model(limit, pgno); 

@app.route('/userlogin/logincheck', methods=['POST'])
def userlogin_check():
    print("User Login Check Controller Accessed")
    return obj.userlogin_check_model(request.form);

