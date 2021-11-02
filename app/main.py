from flask import Flask,render_template,request
import pymongo as pm
app= Flask(__name__)
client = pm.MongoClient("mongodb+srv://mongo-skoreddi:Sravani1234@cluster0.xwp4e.mongodb.net/test")
app.db = client.mflix
movies = []

@app.route('/',methods = ["GET","POST"])
def index():
  return render_template('index.html')

##IMDb movies extensive dataset
