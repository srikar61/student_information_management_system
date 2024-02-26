#!C:\Users\srika\AppData\Local\Programs\Python\Python310\python.exe
print("Content-Type: text/html\n\n")
import sys
sys.path.append('c:\\users\\srika\\appdata\\local\\programs\\python\\python310\\lib\\site-packages')
import pymysql
import cgi,cgitb
cgitb.enable()
form=cgi.FieldStorage()
id1=form.getvalue('studentrollno')
mydb=pymysql.connect(host="localhost",user="root",password="",database="srikar1")
mycursor=mydb.cursor()
mycursor.execute("select * from form")
result=mycursor.fetchall()
hlist=[]
for row1 in result:
    hlist.append(row1[1])
ind=0
if id1 in hlist:
    ind=hlist.index(id1)
else:
    print('''<!DOCTYPE html>
<html>
  <head>
    <title>Student Details</title>
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
<button class="button button1"><a href='home.html' onclick="confirmAction(event,'Home')">Home</a></button>

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
   <script>
    function confirmAction(event, action) {
      event.preventDefault(); // Prevent the default behavior of the anchor tag
      var result = window.confirm("Are you sure you want to " + action + "?");
      if (result) {
        // Perform the action
        
	if (action === "Home") {
          window.location.href = "home.html";
        }
      }
    }
alert("invalid credentials");
  </script>
</html>




''')
    exit(0)
srow=result[ind]
srow2=["studentname:","Rollno","fathername","postaladress","personaladdress","sex","city","course","district","state","pincode","GPA","emailid","DOB","Mobileno"]
print('''<html>
<head>
<style>
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
 
 }
</style>
</head>
<body>
<h1 align=center style="color:dodgerblue;"><b>ADMIN PAGE</b></H1>
<button class="button button1"><a href='home.html' onclick="confirmAction(event,'Home')">Home</a></button>

<button class="button button2"><a href="about.html">About</a></button>

<button class="button button1"><a href="studetails.html">
Student details</a></button>

<button class="button button1"><a href="home.html" onclick="confirmAction(event,'Logout')">
Logout</a></button>



</body>

''')


#print("<html>")
print("<body style='background-image:url(https://images.wisegeek.com/hands-holding-graduation-caps-in-air.jpg);background-repeat:no-repeat;background-size:cover'>")
print("<form method=post action='dfromtable.py'>")
print("<div style='padding-top:90px'>")
print("<table border='1' align='center' style='background-color:white;font-size:20px;font-family:lucida'>")
print("<input type=hidden name='rollno' value={}".format(srow[1]))

print("<tr><td>")
print(srow2[0])
print("</td>")
print("<td>")
print(srow[0])
print("</td></tr>")

print("<tr><td>")
print(srow2[1])
print("</td>")
print("<td >")
print(srow[1])
print("</td></tr>")

print("<tr><td>")
print(srow2[2])
print("</td>")
print("<td>")
print(srow[2])
print("</td></tr>")

print("<tr><td>")
print(srow2[3])
print("</td>")
print("<td>")
print(srow[3])
print("</td></tr>")

print("<tr><td>")
print(srow2[4])
print("</td>")
print("<td>")
print(srow[4])
print("</td></tr>")

print("<tr><td>")
print(srow2[5])
print("</td>")
print("<td>")
print(srow[5])
print("</td></tr>")

print("<tr><td>")
print(srow2[6])
print("</td>")
print("<td>")
print(srow[6])
print("</td></tr>")

print("<tr><td>")
print(srow2[7])
print("</td>")
print("<td>")
print(srow[7])
print("</td></tr>")

print("<tr><td>")
print(srow2[8])
print("</td>")
print("<td>")
print(srow[8])
print("</td></tr>")

print("<tr><td>")
print(srow2[9])
print("</td>")
print("<td>")
print(srow[9])
print("</td></tr>")

print("<tr><td>")
print(srow2[10])
print("</td>")
print("<td>")
print(srow[10])
print("</td></tr>")

print("<tr><td>")
print(srow2[11])
print("</td>")
print("<td>")
print(srow[11])
print("</td></tr>")

print("<tr><td>")
print(srow2[12])
print("</td>")
print("<td>")
print(srow[12])
print("</td></tr>")

print("<tr><td>")
print(srow2[13])
print("</td>")
print("<td>")
print(srow[13])
print("</td></tr>")

print("<tr><td>")
print(srow2[14])
print("</td>")
print("<td>")
print(srow[14])
print("</td></tr>")





print("</table>")
print("</div>")
print("<div style='left-border:100px;align:center;padding-left:700px;'>")
print("<input type=submit value=delete ></input>")
print("</div>")

print("</form>")
print('</body>')
print('''
<script>
    function confirmAction(event, action) {
      event.preventDefault(); // Prevent the default behavior of the anchor tag
      var result = window.confirm("Are you sure you want to " + action + "?");
      if (result) {
        // Perform the action
        
	if (action === "Home") {
          window.location.href = "home.html";
        }
	if (action==="Logout"){
	window.location.href="home.html";
}
      }
    }
  </script>
''')
print("</html>")


