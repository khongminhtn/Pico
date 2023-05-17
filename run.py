import os

from dotenv import load_dotenv
load_dotenv()

from app.blueprints import create_app

if __name__ == '__main__':
  app = create_app()

  # CONFIGURATION
  # MONGO Credential Checking
  mongo_uri = os.environ["MONGO_URI"]
  if not mongo_uri:
    app.logger.debug('MONGO_URI is not set in .env')

  # Set Flask configs
  app.config['MONGO_URI'] = os.environ['MONGO_URI']
  app.config['DEBUG'] = True

  app.run()

