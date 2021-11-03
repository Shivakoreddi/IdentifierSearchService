from flask import Flask,render_template,request,redirect,url_for,session
###from bson.json_util import dumps
###from bson import json_util
###import json
import pymongo as pm
app= Flask(__name__)

client = pm.MongoClient("mongodb+srv://mongo-skoreddi:Sravani1234@cluster0.xwp4e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
app.db = client.mflix
##collection = db["movies"]
##movies=[]
app.secret_key = 'hello'

@app.route('/content',methods=["GET"])
def content():
  if request.method=='GET':
    d = session['d']
    return render_template('content.html',d=d)

@app.route('/',methods = ["GET","POST"])
def index():
  if request.method=='POST':
    movie={}
    id_type = request.form.get("ID_Type")
    id_value = request.form.get("id_value")
    print(id_type)
    print(id_value)
    if id_type=="id":
      data = app.db.movies.find({'imdb.id':int(id_value)})
      for d in data:
        del(d['_id'])
        session['d']=d
        return redirect(url_for('content',d=d))
    else:
      data = app.db.movies.find({'title':str(id_value)})
      for d in data:
        del (d['_id'])
        session['d']=d
        return redirect(url_for('content',d=d))
  return render_template('index.html')


