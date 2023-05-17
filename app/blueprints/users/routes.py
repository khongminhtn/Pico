from flask import Blueprint, request

"""
Structure:
{
		"_id": ObjectId(),
		"username": String,
		"email": String,
		"password": String,  // this should be hashed and salted
		"registrationDate": ISODate()
}
"""

users = Blueprint('user', __name__, url_prefix='/registration')

@users.route('/register', methods=['POST'])
def register():
    pass