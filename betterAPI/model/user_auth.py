from functools import wraps
from flask import make_response, request;
import re, jwt
import mysql.connector
from config.config import dbconfig

class userAuth_M:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host=dbconfig['host'], user=dbconfig['user'], password= dbconfig['password'] , database=dbconfig['database'])
            self.curr = self.conn.cursor(dictionary=True)
            self.conn.autocommit = True
            print("Connection Successful")
        except mysql.connector.Error as e:
                print("Connection Failed", e)

    def token_auth_model(self, endpoint=""):
         def inner1(func):
            @wraps(func)
            def inner2(*args):
                endpoint = request.url_rule
                print("Endpoint Accessed:", endpoint)
                authorization = request.headers.get('Authorization')
                if re.match(r"^Bearer\s+(.+)$", authorization, flags=0):
                    token = authorization.split(" ")[1]
                    try:
                        decoded = jwt.decode(token, "shradha", algorithms=["HS256"])
                    except jwt.ExpiredSignatureError:
                        return make_response({"message":"Token Expired"}, 401)
                    role_id = decoded['role_id']
                    # print(role_id)
                    self.curr.execute(f"SELECT roles FROM acc_with_roles_and_endpoint WHERE endpoint = '{endpoint}'")
                    res = self.curr.fetchall();
                    # print(res)
                    # print(res[0]['roles'])
                    if len(res)>0:
                        allowed = (res[0]['roles'])
                        if str(role_id) in allowed:
                            print("Authorized Access")
                            return func(*args)
                        else:
                            return make_response({"message":"Unauthorized Access"}, 401)
                    else:
                        return make_response({"message":"Unauthorized Access"}, 401)
                else:
                     return make_response({"message":"Unauthorized Access"}, 401)
            return inner2
         return inner1
         

    
         

