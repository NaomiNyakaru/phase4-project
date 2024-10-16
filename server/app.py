from flask import Flask,jsonify,make_response
from flask_migrate import Migrate
from models import User

from models import db
import os

# create flask instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app,db)

@app.route('/')
def home():
    return "Welcome to the API!"

@app.route('/users')
def get_users():
    users = [user.to_dict() for user in User.query.all()]
    return make_response(jsonify(users), 200)

if __name__ == '__main__':
    app.run(debug=True)