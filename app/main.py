from flask import Flask,render_template
app= Flask(__name__)

@app.route('/')
def index():
  return  render_template('index.html')

##mongodb+srv://mongo-skoreddi:<password>@cluster0.xwp4e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
##IMDb movies extensive dataset
