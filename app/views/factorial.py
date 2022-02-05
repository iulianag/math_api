from flask import jsonify, make_response, request
from flask_restful import Resource
from utils import calculator
from models.users import UsersModel


class Factorial(Resource):

    def get(self):
        session_token = request.headers.get('Authorization')
        if not UsersModel.is_registered_token(session_token):
            resp = {"message": "Unauthorized"}
            return make_response(jsonify(resp), 401)
        try:
            n = int(request.args.get('n'))
        except:
            resp = {"message": "Error: Wrong argument type"}
            return make_response(jsonify(resp), 400)
        resp = {"message": "Success",
                "factorial_result": calculator.calculate_factorial(n)}
        return make_response(jsonify(resp), 200)
