#model mai muje 2 code likhne pdege, ik connection ke liye aur ik operations ke liye, isliye connection wala toh constructor m dal dege
import json
import mysql.connector

class userlogin_M:  
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user="Shradha", password="Shradha1402@", database="learningapi")
            self.curr = self.con.cursor(dictionary=True)
            print("Connection Successful")
        except mysql.connector.Error as e:
            print("Connection Failed", e)

    def userlogin_model(self):
        try: 
            self.curr.execute("SELECT * FROM useracc")
            result = self.curr.fetchall()
            if len(result) > 0:
                return result
            else:
                return "No Data Found"
        # return "User Login Model Page"
        except mysql.connector.Error as e:
            return f"Error fetching data: {e}"