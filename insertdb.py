#!C:\Users\srika\AppData\Local\Programs\Python\Python310\python.exe
print("Content-Type: text/html\n\n")
import sys
sys.path.append('c:\\users\\srika\\appdata\\local\\programs\\python\\python310\\lib\\site-packages')

import cgi, cgitb
import pymysql
cgitb.enable() 
import sys
form=cgi.FieldStorage()

name = form.getvalue('name')
rollno = form.getvalue('rollno')
fathername = form.getvalue('fathername')
postaladdress = form.getvalue('postaladdress')
personaladdress = form.getvalue('personaladdress')
sex = form.getvalue('sex')
city = form.getvalue('city')
course = form.getvalue('course')
district = form.getvalue('district')
state = form.getvalue('state')
pincode = form.getvalue('pincode')
gpa = form.getvalue('gpa')
emailid = form.getvalue('emailid')
dob = form.getvalue('dob')
mobileno = form.getvalue('mobileno')

con=pymysql.connect(user='root',password='',host='localhost',
                                database='srikar1')
cur=con.cursor()
sql = "INSERT INTO form (name,rollno,fathername,postaladdress,personaladdress,sex,city,course,district,state,pincode,gpa,emailid,dob,mobileno) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val = (name,rollno,fathername,postaladdress,personaladdress,sex,city,course,district,state,pincode,gpa,emailid,dob,mobileno)
try:
    cur.execute(sql, val)
    con.commit()
    con.close()
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
 body{ }
</style>
<script
  src="https://code.jquery.com/jquery-3.6.1.js"
  integrity="sha256-3zlB5s2uwoUzrXK3BT7AX3FyvojsraNFxCc2vC/7pNI="
  crossorigin="anonymous"></script>
</head>
<body style="background-image:url('https://media.istockphoto.com/id/1349297974/photo/multi-ethnic-group-of-latin-american-college-students-smiling.jpg?b=1&s=170667a&w=0&k=20&c=dkJyrGwyHIkHCWadKMBqsLD5pk-jHH6lpB2Ig23ba-E=');background-size:cover;">
<h1 align=center style="color:dodgerblue;"><b>STUDENT DETAILS</b></H1>
<button class="button button1"><a href='home.html'>Home</a></button>

<button class="button button2"><a href="about.html">About</a></button>

<button class="button button1"><a href="registration.html">
Student Register</a></button>

<button class="button button2"><a href="login.html">Admin Login</a></button>

<br><br><br>

<script type="text/javascript">
        $(window).on('load', AlertMessage());

        function AlertMessage() {
            alert("Data inserted successfully...");
        }
</script>

''')
    
except:
    print(''' 
<html>

  <head>

  
  <style>
  body{
  
background-image:url("https://149350888.v2.pressablecdn.com/wp-content/uploads/students-background.jpg");</style>}
  </script>
  </head>

  <body>

  <form method="POST" action="insertdb.py">





<table cellpadding="2" width="50%" height="80%" bgcolor="#99FFFF" align="center"

  cellspacing="2">


<tr>

  <td colspan=2>

  <center><font size=4><b>Student Registration Form</b></font></center>

  </td>

  </tr>


<tr>

  <td>	Name</td>

  <td><input type=text name="name" id="name" size="30"></td>

  </tr>


<tr>

  <td>Rollno.</td>

  <td><input type=text name="rollno" id="rollno" size="30"></td>

  </tr>






<tr>

  <td>Father Name</td>

  <td><input type="text" name="fathername" id="fathername"

  size="30"></td>

  </tr>

  <tr>

  <td>Postal Address</td>

  <td><input type="text" name="postaladdress" id="postaladdress" size="30"></td>

  </tr>


<tr>

  <td>Personal Address</td>

  <td><input type="text" name="personaladdress" id="personaladdress" size="30"></td>

  </tr>


<tr>

  <td>Sex</td>

  <td><input type="radio" name="sex" value="male" size="10">Male

  <input type="radio" name="sex" value="Female" size="10">Female</td>

  </tr>






<tr>

  <td>City</td>

  <td><select name="city">

  <option value="-1" selected>select..</option>

  <option value="NRT">Narasaraopet</option>

  <option value="CPT">chilakaluripet</option>

  <option value="VNK">Vinukonda</option>

  <option value="GNT">Guntur</option>

  </select></td>

  </tr>


<tr>

  <td>Course</td>

  <td><select name="course">

  <option value="-1" selected>select..</option>

  <option value="B.Tech">B.TECH</option>

  <option value="MCA">MCA</option>

  <option value="MBA">MBA</option>

  <option value="BCA">BCA</option>

  </select></td>

  </tr>


<tr>

  <td>District</td>

  <td><select name="district">

  <option value="-1" selected>select..</option>

  <option value="GNT">Guntur</option>

  <option value="Palnadu">Palnadu</option>

  <option value="BPT">Bapatla</option>


  </select></td>






</tr>


<tr>

  <td>State</td>

  <td><select Name="state">

  <option value="-1" selected>select..</option>

  <option value="AP">Andhra Pradesh</option>

  <option value="other">Other</option>

 
  </select></td>

  </tr>

  <tr>

  <td>PinCode</td>

  <td><input type="text" name="pincode" id="pincode" size="30"></td>
  
  </tr>
 
  <tr>

  <td>GPA</td>

  <td><input type="text" name="gpa" id="gpa" size="30"></td>


</tr>

  <tr>

  <td>EmailId</td>

  <td><input type="text" name="emailid" id="emailid" size="30"></td>

  </tr>






<tr>

  <td>DOB</td>

  <td><input type="date" name="dob" id="dob" size="30"></td>

  </tr>


<tr>

  <td>MobileNo</td>

  <td><input type="text" name="mobileno" id="mobileno" size="30"></td>

  </tr>

  <tr>

  <td><input type="reset"></td>

  <td colspan="2"><input type="submit" value="submit" /></td>

  </tr>

  </table>

  </form>

  </body>
<script>
alert("fill in all the details or student exists already.");
</script>

  </html>
''')



