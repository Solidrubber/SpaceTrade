import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    
    
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return{"message": "Ein User mit dem Namen existiert bereits"}, 400

        user = UserModel(**data)  # .safe_to_db(data['username'], data['password'])
        user.safe_to_db()

        return {"message": "User angelegt"}, 201

