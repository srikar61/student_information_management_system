#!C:\Users\srika\AppData\Local\Programs\Python\Python310\python.exe
print("Content-Type: text/html\n\n")
import sys
sys.path.append('c:\\users\\srika\\appdata\\local\\programs\\python\\python310\\lib\\site-packages')
import pymysql
import cgi,cgitb
cgitb.enable()
form=cgi.FieldStorage()
id1=form.getvalue('rollno')
mydb=pymysql.connect(host="localhost",user="root",password="",database="srikar1")
mycursor=mydb.cursor()
sql ="""DELETE FROM form WHERE rollno='{}'""".format(id1) 
try:
    mycursor.execute(sql)
    mydb.commit()
    print('''<html>
  <head>
    <title>Hello, World!</title>
   <style>
     body{background-color:lightblue;}
     a:link{
   text-color:coral;
text-decoration:none;
   }
a:unvisited{
  color:coral;
}
a:visited{
  color:coral;
}
a:hover{
color:red;
   }
.button {
  border: none;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 17px;
  margin: 4px 2px;
  cursor: pointer;
  float:right;
  
}

.button1 {background-color:transparent;}
.button2 {background-color: transparent;}
 body{
 
 background-size:cover;
 }

   </style>
  </head>
  <body>
<form method="POST" action="rfromtable.py">
<h1 align=center style="color:dodgerblue;"><b>STUDENT DETAILS</b></H1>
<button class="button button1"><a href='home.html'>Home</a></button>

<button class="button button2"><a href="about.html">About</a></button>

<button class="button button1"><a href="registration.html">
Student Register</a></button>



      <div style"padding-top:"90px";border-top:80px;background-color:"dodgerblue";margin:"10px";border:"10px";><br>
      <br><br><br><div align="center"><label >Student Rollno</label>
      <input type"text" name="studentrollno"><br><br>
      <input type="submit" name="submit" align="center">
      </div>
</div>
</form>
  </body>
</html>
''')
except:
    print("database delete error")
