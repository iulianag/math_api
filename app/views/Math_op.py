# from flask import request, jsonify, make_response
# from flask_restful import Resource
# import calculator
# from base import app
#
#
# @app.route('/api/pow', methods=['GET'])
# def get_pow():
#     try:
#         base = int(request.args.get('base'))
#         exp = int(request.args.get('exp'))
#     except:
#         resp = {"message": "Error: Wrong argument type"}
#         return make_response(jsonify(resp), 400)
#     resp = {"message": "Success",
#             "pow_result": base ** exp}
#     return make_response(jsonify(resp), 200)
#
#
# @app.route('/api/factorial', methods=['GET'])
# def get_factorial():
#     try:
#         n = int(request.args.get('n'))
#     except:
#         resp = {"message": "Error: Wrong argument type"}
#         return make_response(jsonify(resp), 400)
#     resp = {"message": "Success",
#             "factorial_result": calculator.calculate_factorial(n)}
#     return make_response(jsonify(resp), 200)
#
#
# @app.route('/api/fibonacci_number', methods=['GET'])
# def get_fibonacci_number():
#     try:
#         n = int(request.args.get('n'))
#     except:
#         resp = {"message": "Error: Wrong argument type"}
#         return make_response(jsonify(resp), 400)
#     resp = {"message": "Success",
#             "fibonacci_number": calculator.calculate_fibonacci_number(n)}
#     return make_response(jsonify(resp), 200)
