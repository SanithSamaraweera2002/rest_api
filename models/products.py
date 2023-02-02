from db import db


class Products(db.Model):

    __tablename__: 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    product_code = db.Column(db.Integer)

    def __int__(self, product_name, product_code):
        self.product_name = product_name
        self.product_code = product_code

    def save_product(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_product_code(cls, product_code):
        return cls.query.filter(cls.product_code == product_code).first()
