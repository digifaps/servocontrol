from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('servo.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         serv_id = request.form['serv_id']
         deg_min = request.form['deg_min']
         deg_max = request.form['deg_max']
         sleep_min = request.form['sleep_min']
         sleep_max = request.form['sleep_max']
         extra = request.form['extra']
         
         with sql.connect("servo_database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO servo (serv_id,deg_min,deg_max,sleep_min,sleep_max,extra)VALUES (?,?,?,?,?,?)",(serv_id,deg_min,deg_max,sleep_min,sleep_max,extra) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("servo_database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from servo")
   
   rows = cur.fetchall();
   return render_template("servolist.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True,host="0.0.0.0")