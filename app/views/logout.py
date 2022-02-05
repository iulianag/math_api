from flask import request, jsonify, make_response
from flask_restful import Resource
from models.users import UsersModel


class Logout(Resource):
    def post(self):
        session_token = request.headers.get('Authorization')
        UsersModel.delete_session_token(session_token)
        return make_response(jsonify({"message": "Bye"}), 200)
