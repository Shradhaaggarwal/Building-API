from app import app
from model.usersignup_M import *
from flask import request, send_from_directory
from datetime import datetime
import os


obj = usersignup_M(); 


@app.route('/usersignup')
def usersignup():
    print("User Signup Controller Accessed")
    return obj.usersignup_model(); 

@app.route('/usersignup/pp/<id>/upload', methods=['PUT'])
def usersignup_pp_post(id):
    pp = request.files['profile_picture']

    datetime_now = str(datetime.now().timestamp()).replace(".","")
    # pp_filename = id + "_" + datetime_now
    ext = pp.filename.split(".")[-1]
    uniqueName = f"{id}_{datetime_now}.{ext}"

    upload_dir = "/static/profile_pics/"
    os.makedirs(upload_dir, exist_ok=True)


    pp.save(os.path.join(upload_dir, uniqueName))
    print("user profile picture uploaded successfully");
    return obj.usersignup_pp_upload_model(id, uniqueName);


@app.route('/pp/<filename>')
def serve_profile_picture(filename):
    return send_from_directory(
        "betterAPI/static/profile_pics", 
        filename
    )