import pytest
from app import create_app
from app.db import db
from app.blueprints.users.routes import users

@pytest.fixture
def app():
	# SETUP
	# Create flask app with testing environment
	app = create_app()
	app.config.update({
		'TESTING': True,
	})
	
	yield app

	# TEARDOWN
	with app.app_context():
		if db.name == 'pico_test':
			collection_names = db.list_collection_names()
			for collection_name in collection_names:
				db[collection_name].drop()

@pytest.fixture
def client(app):
	return app.test_client()

@pytest.fixture
def runner(app):
	return app.test_cli_runner()