import logging

from flask import Flask

def create_app():
  app = Flask(__name__)

  # CONFIGURATION
  # Set logger.debug to pri/nt to console
  app.logger.setLevel(logging.DEBUG)

  return app
