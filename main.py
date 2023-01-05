import os
from flask import render_template,Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html',all_track=[[1,"Fitness Tracker","Number","05-01-2023","100"]]) 

@app.route('/login')
def login():
    return render_template('login.html')

    
if __name__ == '__main__':
  app.debug = True
  app.run() 
