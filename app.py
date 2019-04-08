from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # can also use MySQL, Postgresql, etc.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # only affects extension behaviour
app.secret_key = 'devkey'
api = Api(app)

@app.before_first_request
def create_tables():
	db.create_all()  # will not recreate tables if they already exist

jwt = JWT(app, authenticate, identity)  # default: /auth endpoint

api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/item/Moog%20Modulator - Is like an @app.route decorator
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')	
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(port=5000, debug=True)

# get_json() params: force=True prevents an error if the json does not have the json header (even if json is incorrect)
# get_json() params: silent=True returns Null instead of an error if json is incorrectly formatted