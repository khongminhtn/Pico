import logging
from app import create_app
from app.db import db

def test_config():
  assert not create_app().testing

def test_app_config(app):
  assert app.config['TESTING'] == True
  
def test_db_interaction(app):
  with app.app_context():
    db.users.insert_one({
      'username': 'pytestusername',
      'password': 'pytestpassword'
    })
    result = db.users.find_one({'username': 'pytestusername'})
    username = result['username']
    password = result['password']
    
    logging.basicConfig(level=logging.INFO)
    logging.info(f'{username}, {password}, {db.name}')

    assert db.name == 'pico_test'
    assert username == 'pytestusername'
    assert password == 'pytestpassword'
    