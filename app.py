from flask import Flask,render_template,request
import requests

app= Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/weatherapp",methods=['POST','GET'])
def get_weatherdata():
    apikey="602e11c0c9bf90c661e13498979c2a9d"
    url="https://api.openweathermap.org/data/2.5/weather"

    para={"q":request.form.get("city"),
     "units":"matric",
     "appid":apikey
     }
    
    response=requests.get(url,params=para)
    data=response.json()
    
    return f"data : {data}"

if __name__=="__main__":
    app.run(host="0.0.0.0" , port = 5002)