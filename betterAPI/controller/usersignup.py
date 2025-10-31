from app import app

@app.route('/usersignup')
def usersignup():
    return "User Signup Page"