import json


class TestRegistration:
  def test_register_success(self, client):
    req_headers = {
      'Content-Type': 'application/json'
    }
    data = json.dumps({
      'email': 'pytestusername@email.com',
      'password': 'pytestpassword',
    })
    response = client.post('/register', data=data, headers=req_headers)
    assert response.status_code == 201
    assert b'User register successfully' in response.data

  
  def test_register_failed(self, client):
    req_headers = {
      'Content-Type': 'application/json'
    }
    data = json.dumps({
      # 'email': 'pytestusername@email.com',
      'password': 'pytestpassword',
    })
    response = client.post('/register', data=data, headers=req_headers)
    assert response.status_code == 400
    assert b'Missing required field' in response.data
