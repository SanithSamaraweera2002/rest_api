from flask import Flask
from flask_restful import Api
from db import db


from resource.hello_get import HelloGet
from resource.hello_post import HelloPost


application = Flask(__name__)

api = Api(application)

#application.config['SQLALCHEMY_DATABASE_URI'] = os.environ['database_url']
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin123@localhost:5432/rest_api_tutorial'

db.init_app(application)
with application.app_context():
    db.create_all()

api.add_resource(HelloGet,'/get/<string:data>')
api.add_resource(HelloPost,'/post')

if __name__ =='__main__':
    application.run(debug=True, port=3002)

