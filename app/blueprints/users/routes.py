from flask import current_app, Blueprint, request, jsonify
from .model import Users
from bson import ObjectId
from typing import Tuple

# Initialise blueprint for users
users = Blueprint('user', __name__)

# Create an instance of the Users model
users_model = Users()

# User register
@users.route('/register', methods=['POST'])
def register() -> Tuple[dict, int]:
	"""
	Reigsters a new user with the given email and password.

	This function extracts the email and password from the incoming JSON request.
	It then attempts to create a new user with hashed password in the Users model. 
	If successful, it returns a JSON response with the user's ID and a success message. 
	If any data is missing or an error occurs, it returns a JSON error message and an appropriate HTTP status code.

	Returns:
			A tuple containing a JSON resposne and a HTTP status code.

	Raises:
			Exeception: If an error occurs while creating the user.
	"""

	# Get data from flask's request body
	registration_data = request.get_json()

	# Extract required data
	email: str = registration_data.get('email')
	password: str = registration_data.get('password')

	# Validate reg data
	if not email or not password:
		return jsonify({'error': 'Missing required field'}), 400

	try:
		# Create new user 
		user_id: ObjectId = users_model.create_user(email, password)

		# Validate the success of user creation
		if not user_id:
				return jsonify({'error': 'User creation failed'}), 500
		
		# Return success
		return jsonify({'message': 'User register successfully', 'user_id': str(user_id)}), 201
	
	except Exception as e:
		current_app.logger.error(f'Error registering user: {e}')
		return jsonify({'error': 'An error occured while registering user'}), 500