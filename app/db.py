from werkzeug.local import LocalProxy
from flask import current_app, g
from flask_pymongo import PyMongo

def get_db():
  """
  Configuration method to return db instance using proxy

  """
  db = getattr(g, "_database", None)

  if db is None:
    
    # Use database according to DEVELOPMENT or PRODUCTION evironment.
    db = g._database = PyMongo(current_app).cx[current_app.config['DB_NAME']]
      

    # Verify database connection
    try:
      db.client.server_info()
      current_app.logger.debug(f"MongoDB successfully connected to {db.name}")
    except Exception as e:
      current_app.logger.error(f"MongoDB connection failed: {e}")
  return db

db = LocalProxy(get_db)

