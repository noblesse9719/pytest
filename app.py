from flask import Flask
import mysql.connector
import json

app = Flask(__name__)

@app.route('/')
def index():
  return "some alien world!" 

@app.route('/db')
def dbquery():
  mydb = mysql.connector.connect(host="18.220.248.20",user="pytest",password="pytest",database="pytest")
  mycursor = mydb.cursor()
  mycursor.execute("select * from test")
  myresult = mycursor.fetchall()
  row_headers=[x[0] for x in mycursor.description]
  json_data=[]
  for result in myresult:
      json_data.append(dict(zip(row_headers,result)))
  return json.dumps(json_data)


def fc(x):
    return x.capitalize()

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
