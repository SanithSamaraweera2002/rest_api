from flask_restful import Resource
from flask import request
from models.users import Users
from werkzeug.security import generate_password_hash


class RegisterUser(Resource):
    def post(self):
        data = request.get_json()

        user = Users.find_by_user_name(data['username'])
        if user:
            return f"User already exists", 400

        hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256', salt_length=8)

        # user = Users.find_by_user_name(user_name=data['user_name'])
        # user.delete_user()

        # return f' successfully deleted user {user.emp_name}', 200
        user = Users(user_name=data['username'], emp_name=data['empname'], pass_word=hashed_password)
        user.save_user()

        return f'successfully added user {user.emp_name}', 201

