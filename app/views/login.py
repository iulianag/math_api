from flask import request, jsonify, make_response
from flask_restful import Resource
from models.users import UsersModel
from utils.authorization import validate_credentials, generate_session_token


class Login(Resource):
    def post(self):
        user_id = request.form.get('username')
        password = request.form.get('password')

        validate_credentials_result = validate_credentials(user_id, password)
        if validate_credentials_result[1] != 200:
            return make_response(jsonify(validate_credentials_result[0]), validate_credentials_result[1])

        new_token = generate_session_token()

        UsersModel.update_session_token(user_id, password, new_token)

        return make_response(jsonify({"token": new_token}), 201)
