
from flask_restful import Resource

class Count(Resource):
    def __init__(self, cnt):
        cnt += 1

    def post(self):
        return "Count is post : " + str(self.nSum(self.cnt))

    def get(self):
        return "Count is Get : "

    def nSum(self, a):
        return a+1
