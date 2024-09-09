#!C:\Python312\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")

print("<html>")
print("<body>")

Form=cgi.FieldStorage()
fName=Form.getvalue('name')
fAge=Form.getvalue('age')
fphone=Form.getvalue('phone')
fEmail=Form.getvalue('email')
fplace=Form.getvalue('place')
fComment=Form.getvalue('comment')


print("<h1>Thank you for register!!!</h1>")
print(fName,fEmail,fphone,fAge,fplace,fComment)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ff"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Players(name,age,phone,email,place,comment)VALUES(%s,%s,%s,%s,%s,%s)"
val=(fName,fEmail,fphone,fAge,fplace,fComment)

mycursor.execute(sql,val)
mydb.commit()

print("</body>")
print("</html>")
