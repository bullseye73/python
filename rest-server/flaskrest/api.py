# -*- conding:utf-8 -*-

from flask import Flask, render_template
from flask_restful import Api

from api.count import Count
from api.createUser import CreateUser

app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)

api.add_resource(CreateUser, '/user')
api.add_resource(Count, '/count')

@app.route("/", methods=['POST'])
def main():
    return render_template('hello.html')
    #return "Hello World flask!"

if __name__ == '__main__':
    app.run(host="192.168.219.129", port="8000", debug=True)
