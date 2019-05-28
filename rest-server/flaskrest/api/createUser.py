from flask_restful import Resource

class CreateUser(Resource):
    def post(self):
        return {'status': 'post success'}
    def get(self):
        return {'status' : 'get success'}