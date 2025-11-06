#model mai muje 2 code likhne pdege, ik connection ke liye aur ik operations ke liye, isliye connection wala toh constructor m dal dege
import json
import jwt
from datetime import datetime, timedelta 
import mysql.connector
from config.config import dbconfig
from flask import make_response; 

class userlogin_M:  
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host=dbconfig['host'], user=dbconfig['user'], password= dbconfig['password'] , database=dbconfig['database'])
            self.curr = self.conn.cursor(dictionary=True)
            self.conn.autocommit = True; 
            print("Connection Successful")
        except mysql.connector.Error as e:
            print("Connection Failed", e)

    def userlogin_model(self):
        try: 
            self.curr.execute("SELECT * FROM useracc")
            result = self.curr.fetchall()
            if len(result) > 0:
                # return result
                return make_response({"data": result}, 200) #200 is status code for success
            else:
                return {"message":"No Data Found"}
        # return "User Login Model Page"
        except mysql.connector.Error as e:
            return f"Error fetching data: {e}"
        

    def userlogin_post_model(self,data):
        try:
            query = "INSERT INTO USERACC (user_name, user_pass) VALUES (%s, %s)"
            values = (data['user_name'], data['user_pass'])
            self.curr.execute(query, values)
            return {"message":"User added successfully"}
        except mysql.connector.Error as e:
            return f"Error inserting data: {e}"
        
    
    def userlogin_put_model(self,data):
        try: 
            query = "UPDATE USERACC SET user_name=%s, user_pass=%s WHERE id = %s"
            values = (data['user_name'], data['user_pass'], data['id'])
            self.curr.execute(query, values)
            if self.curr.rowcount>0:
                return {"message":"goood"}
            else: 
                return {"message":"No record found to update"}
        except mysql.connector.Error as e:
            return f"Error updating data: {e}"
        

    def userlogin_delete_model(self, id):
        try: 
            query = "DELETE FROM useracc WHERE id=%s"
            values = (id,)
            self.curr.execute(query, values)
            if self.curr.rowcount>0:
                return {"message":"Deleted Successfully"}
            else:
                return {"message":"No record found to delete"}
            
        except mysql.connector.Error as e:
            return f"Error deleting data: {e}"
        

    def userlogin_patch_model(self, data, id):
        try:
            query = "UPDATE useracc SET "
            
            for key in data:
                query += f"{key}= '{data[key]}',"
            
            query = query[:-1] + " WHERE id=%s"
            values = (id,)
            self.curr.execute(query, values)
            # return query
            if self.curr.rowcount>0:
                return {"message":"Patched Successfully"}
            else:
                return {"message":"No record found to patch"}
        except mysql.connector.Error as e:
            return f"Error patching data: {e}"
        

    def userlogin_pagination_model(self, limit, pgno):
        limit = int(limit)
        pgno = int(pgno)
        try:
            offset = pgno*limit - limit;
            query = "SELECT * FROM useracc LIMIT %s OFFSET %s"
            values = (limit, offset);
            self.curr.execute(query, values)
            result = self.curr.fetchall()
            if(len(result)>0):
                return make_response({"data": result, "limit": limit, "pageno": pgno}, 200)
            else:
                return make_response({"message":"No data found"}, 202)
        except mysql.connector.Error as e:
            return f"Error: {e}"
        
    def userlogin_check_model(self, data):
        try:
            query = "SELECT id, user_name, role_id, pp_path FROM useracc WHERE user_name = %s AND user_pass = %s";
            values = (data['user_name'], data['user_pass'])
            self.curr.execute(query, values)
            res = self.curr.fetchall()
            if len(res) == 0:
                return make_response({"message": "Invalid username or password"}, 401)
            userdata = res[0]
            exp_date = int((datetime.now() + timedelta(minutes=15)).timestamp())
            payload = {
                "id": userdata['id'],
                "user_name": userdata['user_name'],
                "role_id": userdata['role_id'],
                "exp": exp_date
            }
            jwttoken = jwt.encode(payload, "shradha", algorithm="HS256")
            return make_response({"token": jwttoken}, 200)
        except mysql.connector.Error as e:
            return f"Error: {e}"
            