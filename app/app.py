from flask_restful import Api
from views.base import app
from views import factorial, fibonacci, pow_op, login, logout
from models.base import Base, engine
from utils.authorization import add_admin

api = Api(app)
Base.metadata.create_all(engine)
add_admin()

api.add_resource(login.Login, '/api/login')
api.add_resource(logout.Logout, '/api/logout')
api.add_resource(pow_op.PowOp, '/api/pow')
api.add_resource(factorial.Factorial, '/api/factorial')
api.add_resource(fibonacci.Fibonacci, '/api/fibonacci')


if __name__ == "__main__":
    app.config['SERVER_NAME'] = "192.168.112.129:8082"
    app.run()
