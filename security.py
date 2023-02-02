from werkzeug.security import check_password_hash

from models.users import Users


def authenticate(username, password):
    user = Users.find_by_user_name(username)

    if user and check_password_hash(user.pass_word, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return Users.find_by_id(user_id)




