from models.users import UsersModel
import re
import random
import string


def validate_username(username):
    if len(username) < 3:
        return {"message": "username must have more than 2 characters"}, 400
    else:
        match = re.search(r"^[\w.-]+$", username)
        if not match:
            return {"message": "Invalid characters for username"}, 400
        elif UsersModel.is_registered_user(username):
            return {"message": "username already used"}, 400
        else:
            return {}, 200


def validate_password(password):
    if len(password) < 6:
        return {"message": "password must have more than 5 characters"}, 400
    else:
        match = re.search(r"^[\w.-]+$", password)
        if not match:
            return {"message": "Invalid characters for password"}, 400
        else:
            return {}, 200


def validate_credentials(username, password):
    if not UsersModel.is_registered_user(username):
        return {"message": "Unknown username"}, 400
    elif not UsersModel.are_registered_credentials(username, password):
        return {"message": "Wrong password"}, 400
    else:
        return {}, 200


def generate_session_token():
    letters = string.hexdigits
    token = ''.join(random.choice(letters) for i in range(10))
    while UsersModel.is_registered_token(token):
        token = ''.join(random.choice(letters) for i in range(10))
    return token


def validate_register_data(username, password):
    validate_username_result = validate_username(username)
    if validate_username_result[1] != 200:
        return validate_username_result

    validate_password_result = validate_password(password)
    if validate_password_result[1] != 200:
        return validate_password_result

    return {}, 200


def add_new_user(username, password):
    validate_request_data = validate_register_data(username, password)
    if validate_request_data[1] != 200:
        return validate_request_data

    token = generate_session_token()

    new_user = UsersModel(username, password, token)
    new_user.add_user(username=username, password=password)
    return {"token": token}, 201


def add_admin():
    username = 'admin'
    password = 'admin'
    if not UsersModel.are_registered_credentials(username, password):
        UsersModel.add_user(username=username, password=password)
    return 0




