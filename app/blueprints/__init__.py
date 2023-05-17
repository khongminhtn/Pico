import logging

from flask import Flask
from .users.routes import users

def create_app():
  app = Flask(__name__)

  # CONFIGURATION
  # Set logger.debug to pri/nt to console
  app.logger.setLevel(logging.DEBUG)

  app.register_blueprint(users)

  return app
