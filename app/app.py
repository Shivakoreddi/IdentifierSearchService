from flask import Flask,render_template,request
import pymongo as pm
app= Flask(__name__)


@app.route('/',methods = ["GET","POST"])
def index():
  return render_template('index.html')

##IMDb movies extensive dataset
