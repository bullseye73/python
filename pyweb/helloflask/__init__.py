from flask import Flask, g, make_response, Response

app = Flask(__name__)
app.debug = True

# request시 먼저 실행.
# @app.before_request
# def before_request():
#     print("before_request !!")
#     g.str = "한글"

# @app.route("/gg")
# def helloworld2():
#     return "Hello Flask world!!" + getattr(g, 'str', '111') #'111'은 default 값.
@app.route('/test_wsgi')
def test_wsgi():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        header = [('Content-Type', 'text/plain'), 
                  ('Content-Length', str(len(body))) ]
        start_response('200 OK', header)
        return [body]
    return make_response(application)

@app.route('/res1')
def res1():
    custom_res = Response("Custom Response", 200, {'test':'ttttttt'})
    return make_response(custom_res)

@app.route("/")
def helloworld():
    return "Hello Flask world!!"


    