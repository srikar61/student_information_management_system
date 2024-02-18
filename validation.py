#!C:\Users\srika\AppData\Local\Programs\Python\Python310\python.exe
print("Content-Type: text/html\n\n")
import sys
sys.path.append('c:\\users\\srika\\appdata\\local\\programs\\python\\python310\\lib\\site-packages')
import cgi, cgitb
import pymysql
cgitb.enable()
mydb=pymysql.connect(user='root',password='',host='localhost',database='srikar1')
mycursor=mydb.cursor()
form=cgi.FieldStorage()
mycursor.execute("select * from login")
result=mycursor.fetchall()
maillist=[]
for row in result:
    maillist.append(row[0])
username = form.getvalue('username')
password = form.getvalue('password')
if username in maillist:
    i=maillist.index(username)
    row=result[i]
    if (row[1]==password):

        print('''
<!DOCTYPE html>
<html>
<head>
  <title>ADMIN PAGE</title>
  <style>
    a:link {
      color: coral;
      text-decoration: none;
    }
    a:visited {
      color: coral;
    }
    a:hover {
      color: red;
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
      float: right;
    }
    .button1 {
      background-color: transparent;
    }
    .button2 {
      background-color: transparent;
    }
    body {
      background-image: url("https://img.freepik.com/free-vector/students-with-diplomas-celebrating-graduation-campus-park_1262-20691.jpg?w=1380&t=st=1670129853~exp=1670130453~hmac=208a3ba6574b7853a43bf023c8e8500024834546071ef497442f54ad8924a3d3");
      background-size: cover;
    }
  </style>
</head>
<body>
  <h1 align="center" style="color: dodgerblue;"><b>ADMIN PAGE</b></h1>
  <button class="button button1"><a href="home.html" onclick="confirmAction(event, 'Home')">Home</a></button>
  <button class="button button2"><a href="about.html">About</a></button>
  <button class="button button1"><a href="studetails.html">Student details</a></button>
  <button class="button button1"><a href="home.html" onclick="confirmAction(event, 'Logout')">Logout</a></button>

  <script>
    function confirmAction(event, action) {
      event.preventDefault(); // Prevent the default behavior of the anchor tag
      var result = window.confirm("Are you sure you want to " + action + "?");
      if (result) {
        // Perform the action
        if (action === "Logout") {
          window.location.href = "home.html";
        }
	if (action === "Home") {
          window.location.href = "home.html";
        }
      }
    }
  </script>
</body>
</html>

''')
        
        
        # print("<body style='background-color:white;'</body>")
        print("<h2 style='color:black;font-weight:bold;margin-left:550px;'>Welcome &ensp;  ",row[0],"</h2>")
        
    else:
        print(''' 
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Login</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
     .button {
      border: none;
      padding: 10px 20px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      margin: 0 5px;
      cursor: pointer;
      background-color: #007bff;
      color: #fff;
      border-radius: 5px;
      float: right;
      margin-top: 10px;
      transition: background-color 0.3s;
  }
  .button  a{
    color: white;
    text-decoration: none;
  }
  .button:hover {
      background-color: #0056b3;
  }
  header {
      background-color: #f8f9fa;
      padding: 10px 0;
      text-align: center;
  }
.container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 80vh;
  }
  .card {
      width: 400px;
     
  }
</style>
              <script>
              window.onload=function(){
              alert("Incorrect Password!");
              }
              </script>
</head>
<body class="bg-light">
    <header>

        <button class="button"><a href='home.html'>Home</a></button>
        <button class="button"><a href="about.html">About</a></button>
        <button class="button"><a href="registration.html">Student Register</a></button>
        <button class="button"><a href="signup.html">Admin Signup</a></button>
        
        </header>
<div class="container">
    <div class="row justify-content-center mt-5">
        <div class="col-md-6">
            <div class="card shadow">
                <div class="card-body">
                    <h5 class="card-title" style="text-align: center;">Login</h5>
                    <form action="validation.py">
                        <div class="mb-3">
                            <label for="username" class="form-label">Username</label>
                            <input type="text" class="form-control" id="username" name="username" required>
                        </div>
                        <div class="mb-3">
                            <label for="password" class="form-label">Password</label>
                            <input type="password" class="form-control" id="password" name="password" required>
                        </div>
                        <button type="submit" class="btn btn-primary">Login</button>

                        <a href="signup.html" style="margin-left: 10px;">Signup</a>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

''')
      
         
else:
    print('''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Login</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
     .button {
      border: none;
      padding: 10px 20px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      margin: 0 5px;
      cursor: pointer;
      background-color: #007bff;
      color: #fff;
      border-radius: 5px;
      float: right;
      margin-top: 10px;
      transition: background-color 0.3s;
  }
  .button  a{
    color: white;
    text-decoration: none;
  }
  .button:hover {
      background-color: #0056b3;
  }
  header {
      background-color: #f8f9fa;
      padding: 10px 0;
      text-align: center;
  }
.container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 80vh;
  }
  .card {
      width: 400px;
     
  }
</style>
              <script>
              window.onload=function(){
              alert("User doesn't exist!");
              }
              </script>
</head>
<body class="bg-light">
    <header>

        <button class="button"><a href='home.html'>Home</a></button>
        <button class="button"><a href="about.html">About</a></button>
        <button class="button"><a href="registration.html">Student Register</a></button>
        <button class="button"><a href="signup.html">Admin Signup</a></button>
        
        </header>
<div class="container">
    <div class="row justify-content-center mt-5">
        <div class="col-md-6">
            <div class="card shadow">
                <div class="card-body">
                    <h5 class="card-title" style="text-align: center;">Login</h5>
                    <form action="validation.py">
                        <div class="mb-3">
                            <label for="username" class="form-label">Username</label>
                            <input type="text" class="form-control" id="username" name="username" required>
                        </div>
                        <div class="mb-3">
                            <label for="password" class="form-label">Password</label>
                            <input type="password" class="form-control" id="password" name="password" required>
                        </div>
                        <button type="submit" class="btn btn-primary">Login</button>

                        <a href="signup.html" style="margin-left: 10px;">Signup</a>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''')