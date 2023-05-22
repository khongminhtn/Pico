import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
  try:
    MONGO_URI = os.environ["MONGO_URI"]
  except KeyError:
    raise(RuntimeError('MONGO_URI env is not set, set it in .env file'))
  DEBUG = True
  DEVELOPMENT = True

class ProductionConfig(Config):
  DB_NAME = 'pico'
  DEBUG = False
  DEVELOPMENT = False

class DevelopmentConfig(Config):
  DB_NAME = 'pico_test'

