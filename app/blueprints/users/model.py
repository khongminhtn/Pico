from werkzeug.security import generate_password_hash
from typing import Optional
from bson.objectid import ObjectId
from flask import current_app

from app.db import db

class Users:
  def create_user(self, email: str, password: str) -> Optional[ObjectId]:
    '''
    Create a new user and hashing the password after checking for existing user 

    Args:
      email (str): The email of the new user.
      password (str): The password of the new user.

    Returns:
      str: The user_id of the created user if successful, otherwise None
    '''
    # Check if the user already exists
    if self.user_exists(email):
      return None
    
    hashed_password: str = self.password_hashing(password)
    
    # Store the user information
    new_user = {
      'email': email,
      'password': hashed_password,
    }

    try:
      # Add new user
      result = db.users.insert_one(new_user)
      user_id = result.inserted_id
    except Exception as e:
      current_app.logger.debug(f'Add new user failed: {e}')  

    return user_id


  def user_exists(self, email: str) -> bool:
    '''
    Check if a user with the given email exists in the 'users' collection

    Args:
      email (str): The email of the user

    Returns:
      bool: True if user with given email exists, else False
    '''
    return db.users.find_one({'email': email}) is not None
  

  def password_hashing(self, password: str) -> str:
    '''
    Hashes a password using strong hash function

    Args: 
      password: (str): The password to be hashed

    Returns:
      str: The hashed password.
    '''
    return generate_password_hash(password)