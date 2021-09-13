from flask import Flask,render_template,request
from youtube_search import YoutubeSearch
from pytube import YouTube
from flask_cors import CORS
from corona_python import Country
app = Flask(__name__,template_folder='template')
CORS(app)
@app.route('/',methods=["POST","GET"])
def main():

    return render_template("index.html")
@app.route('/save',methods=["POST","GET"])
def save():
    h2=request.args.get('val')
    file1 = open('myfile.txt', 'w')
    file1.write(h2) 
    return "Saved" 
    
    
@app.route('/read',methods=["POST","GET"])
def read():
    file1 = open('myfile.txt', 'r') 
    return file1.read()
    file1.close() 
  
if __name__ == "__main__":    
   app.run(debug=True)
