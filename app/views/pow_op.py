from flask import jsonify, make_response, request
from flask_restful import Resource
from models.users import UsersModel


class PowOp(Resource):
    def get(self):
        session_token = request.headers.get('Authorization')
        if not UsersModel.is_registered_token(session_token):
            resp = {"message": "Unauthorized"}
            return make_response(jsonify(resp), 401)
        try:
            base = int(request.args.get('base'))
            exp = int(request.args.get('exp'))
        except:
            resp = {"message": "Error: Wrong argument type"}
            return make_response(jsonify(resp), 400)
        resp = {"message": "Success",
                "pow_result": base ** exp}
        return make_response(jsonify(resp), 200)
