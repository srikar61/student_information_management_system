#!C:\Users\srika\AppData\Local\Programs\Python\Python310\python.exe
print("Content-Type: text/html\n\n")
import sys
sys.path.append('c:\\users\\srika\\appdata\\local\\programs\\python\\python310\\lib\\site-packages')
import cgi, cgitb
import pymysql
cgitb.enable() 
form=cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

con=pymysql.connect(user='root',password='',host='localhost',
                                database='srikar1')
cur=con.cursor()
cur.execute("select * from login")
result=cur.fetchall()
maillist=[]
for row in result:
    maillist.append(row[0])
if username in maillist:
    print('''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Signup</title>
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
</style><script> window.onload=function(){
          alert('user already exists!');
}</script>
</head>
<body class="bg-light">
    <header>

        <button class="button"><a href='home.html'>Home</a></button>
        <button class="button"><a href="about.html">About</a></button>
        <button class="button"><a href="registration.html">Student Register</a></button>
        <button class="button"><a href="login.html">Admin Login</a></button>
        
        </header>
<div class="container">
    <div class="row justify-content-center mt-5">
        <div class="col-md-6">
            <div class="card shadow">
                <div class="card-body">
                    <h5 class="card-title" style="text-align: center;">Signup</h5>
                    <form action="insertdb2.py">
                        <div class="mb-3">
                            <label for="username" class="form-label">Username</label>
                            <input type="text" class="form-control" id="username" name="username" required>
                        </div>
                        <div class="mb-3">
                            <label for="password" class="form-label">Password</label>
                            <input type="password" class="form-control" id="password" name="password" required>
                        </div>
                        <div class="mb-3">
                            <label for="password" class="form-label">Confirm Password</label>
                            <input type="password" class="form-control" id="password" name="password2" required>
                        </div>
                        <button type="submit" class="btn btn-primary">Sign up</button>

                        <a href="login.html" style="margin-left: 10px;">Login</a>
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
    exit(0)
sql = "INSERT INTO login (username,password) VALUES(%s, %s)"
val = (username, password)
cur.execute(sql, val)
con.commit()
con.close()
print('''<!DOCTYPE html>
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
      <script> window.onload=function(){
          alert('Signed up Successfully!');
}</script>
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

    

