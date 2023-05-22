import logging
import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from .blueprints.users.routes import users

def create_app():
  """
  Create and configure the Flask application.
  
  Returns:
      app: The Flask application.
  """
  app = Flask(__name__)

  # load config
  app.logger.setLevel(logging.DEBUG)
  try:
    if os.environ['ENV'] == 'dev':
      app.config.from_object('app.config.DevelopmentConfig')
    elif os.environ['ENV'] == 'prod':
      app.config.from_object('app.config.ProductionConfig')
  except Exception as e:
    app.logger.debug('ENV is not set properly, check out .env file {e}')

  # register blueprints
  app.register_blueprint(users)

  return app
