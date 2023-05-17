from werkzeug.local import LocalProxy
from flask import current_app, g
from flask_pymongo import PyMongo

def get_db():
  """
  Configuration method to return db instance using proxy

  """
  db = getattr(g, "_database", None)

  if db is None:
    db = g._database = PyMongo(current_app.db)

    # Verify database connection
    try:
      db_info = db.client.server_info()
      current_app.logger.debug("MongoDB connection successful {db_info}")
    except Exception as e:
      current_app.logger.error("MongoDB connection failed: {e}")
  
  return db

db = LocalProxy(get_db)

