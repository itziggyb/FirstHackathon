# ONLY WORKS WHEN URL IS http://127.0.0.1:5000/index.html  idk why 


from flask import Flask, request, render_template, session, flash, redirect, url_for
from flask.helpers import url_for
from pytube import YouTube
import secrets



app = Flask(__name__)

app.secret_key = "0B526E1787DD5191C10356C64DF36256"



@app.route("/index.html", methods = ["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/downloadpath.html", methods = ["GET", "POST"])
def download_video():
    if request.method == 'POST':
        session['link'] = request.form.get('url')
        try:
            url = YouTube(session['link'])
            url.check_availability()
        except:
            return render_template("error.html")
        return render_template("download.html",url=url,vid=session['link'])  
    return render_template("downloadpath.html")
   
   



if __name__ == "__main__": 
    app.run(debug = True)
    