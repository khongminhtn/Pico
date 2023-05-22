import os
from flask_pymongo import PyMongo

from dotenv import load_dotenv
load_dotenv()

from app import create_app


if __name__ == '__main__':
  """
  When run as a standalone program, this script creates a Flask application, 
  sets its configuration, and then runs it.
  """
  app = create_app()
  app.run()

