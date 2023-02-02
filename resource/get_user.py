from flask_restful import Resource
from models.users import Users


class GetUser(Resource):
    def get(self, data):

        user = Users.find_by_user_name(user_name=data)

        # user.delete_user()

        # return 'User Deleted'

        return {
            'name': user.emp_name,
            'password': user.pass_word
        }

