from db import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    emp_name = db.Column(db.String(100))
    pass_word = db.Column(db.String(100))

    def __int__(self, user_name, emp_name, pass_word):
        self.user_name = user_name
        self.emp_name = emp_name
        self.pass_word = pass_word

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_user_name(cls,user_name):
        return cls.query.filter(cls.user_name == user_name).first()

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter(cls.id == user_id).first()


