from flask import Flask,render_template,request
import hashlib
import json
from flask_cors import CORS
from corona_python import Country
app = Flask(__name__,template_folder='template')
CORS(app)
@app.route('/',methods=["POST","GET"])
def main():
    return render_template("login.html")
    
@app.route('/login',methods=["POST","GET"])
def login():
    usern1=request.args.get('usern')
    userp1=request.args.get('userp')
   
    file1 = open('pass/'+usern1+'.txt', 'r') 
    key= file1.read()
    file1.close() 
    if key==userp1:
       file2 = open('pass/'+usern1+'_type.txt', 'r') 
       key2= file2.read()
       file1.close() 
    else:
      return "Password Or Username Unvalid!!"
    if key2=="admin":
       return render_template("index.html")
    
    else:
      return render_template("user.html")
    
    
@app.route('/save',methods=["POST","GET"])
def save():
    h2=request.args.get('val')
    dat=request.args.get('dt')
    file11 = open('years/'+dat+'.html', 'a')
    file11.write(h2+'\n') 
    file2 = open('db.html', 'a')
    file2.write(h2+'\n') 
    file2.close()
    
    return "Saved" 
@app.route('/abc',methods=["POST","GET"])
def abc():
    h2x=request.args.get('val2')
    datx=request.args.get('dt2')
    file11x = open('years/'+datx+'.html', 'w')
    file11x.write(h2x) 
    file11x.close()
    file2x = open('db.html', 'w')
    file2x.write(h2x) 
    file2x.close()
    return "saved"
    
@app.route('/read',methods=["POST","GET"])
def read():
    file1 = open('db.html', 'r') 
    return file1.read()
    file1.close() 
    
@app.route('/year',methods=["POST","GET"])
def year():
    y=request.args.get('year')
    m=request.args.get('month')
   
    file3 = open('years/'+m+y+'.html', 'r') 
    return file3.read()
    file3.close() 
@app.route('/usersave',methods=["POST","GET"])
def usave():
    usern=request.args.get('usern')
    userp=request.args.get('userp')
    usert=request.args.get('usert')
    
    file3x = open('pass/'+usern+'.txt', 'w')
    file3x.write(userp) 
    file4x = open('pass/'+usern+'_type.txt', 'w')
    file4x.write(usert) 
    return "User:("+usern+") Registrated authorized As: "+usert+""


if __name__ == "__main__":    
   app.run(debug=False)
