from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Better API!"

# import betterAPI.controller.userlogin as userlogin
# from controller import userlogin,usersignup 
if __name__ == '__main__':
    app.run(debug=True)


from controller import userlogin_C, usersignup_C



