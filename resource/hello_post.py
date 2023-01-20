from flask_restful import Resource
from flask import request
from models.users import Users


class HelloPost(Resource):
    def post(self):
        data = request.get_json()

        user = Users.find_by_user_name(user_name=data['user_name'])
        user.delete_user()

        return f' successfully deleted user {user.emp_name}', 200
        #user = Users(user_name=data['user_name'], emp_name=data['emp_name'], pass_word=data['pass_word'])
        u#ser.save_user()

        #return f'successfully added user {user.emp_name}', 201

