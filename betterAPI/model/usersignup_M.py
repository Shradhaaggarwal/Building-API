import mysql.connector
from flask import make_response
from config.config import dbconfig
class usersignup_M:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host=dbconfig['host'], user=dbconfig['user'], password= dbconfig['password'] , database=dbconfig['database'])
            self.curr = self.conn.cursor(dictionary=True)
            self.conn.autocommit = True;
            print("Connection Successful")
        except mysql.connector.Error as e:
            print("Connection Failed", e)


    def usersignup_model(self):
        return make_response({"message":"User Signup Model Page"})
    
    def usersignup_pp_upload_model(self, id, path):
        try:
            query = "UPDATE useracc SET pp_path=%s WHERE id=%s";
            values = (path, id);  
            self.curr.execute(query, values);
            if self.curr.rowcount>0:
                return make_response({"message":"Profile picture uploaded successfully"}, 200)
            else:
                return make_response({"message":"No record found to update profile picture"}, 202)
        except mysql.connector.Error as e:
            return f"Error updating profile picture: {e}"