from flask import Flask

app = Flask(__name__)

@app.route("/") #decorator
@app.route("/index") 

def hello():
    
    return "Hello World!!"

if __name__=="__main__":
    #app.run()
    # or app.run(host='192.168.219.100')
    app.run(host='0.0.0.0', port='5000')     