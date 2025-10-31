from app import app

@app.route('/userlogin')
def userlogin():
    return "User Login Page"