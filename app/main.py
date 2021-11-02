from flask import Flask,render_template
app= Flask(__name__)

@app.route('/')
def index():
  return  "<h1>Welcome to Movies Identifier Search Service</h1>"
##mongodb+srv://mongo-skoreddi:<password>@cluster0.xwp4e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
##IMDb movies extensive dataset
