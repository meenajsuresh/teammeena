from flask import Flask,request,render_template

from flask_mysqldb import  MySQL


mysql =  MySQL()
app= Flask(__name__)
app.config["MYSQL_DATABASE_USER"]="root"
app.config["MYSQL_DATABASE_PASSWORD"]="1234"
app.config["MYSQL_DATABASE_DB"]="names"
app.config["MYSQL_DATABASE_HOST"]="localhost"
mysql.init_app(app)

@app.route('/',methods=['GET','POST'])
def get_data():
  if request.method=='POST':
    first_name=request.form['fname']
    last_name=request.form['lname']
    emailid=request.form['emailid']
    connection = mysql.connection()
    cursor = connection.cursor()
    query="INSERT INTO names_tbl(f_name,l_name,e_id) VALUES(%s,%s,%s)"
    cursor.execute(query,(first_name,last_name,email_id))
    connection.commit()
    if connection:
      print("connection")
    else:
      print("connection error")

  return render_template("userdetails.html")

if __name__=='__main__':
  app.run(debug=True)
if connection:
  print("connection")
else:
  print("connection error")