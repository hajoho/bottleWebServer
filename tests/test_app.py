from bottledemo import app
from webtest import TestApp

def test_hello_endpoint():
    test_app = TestApp(app)
    response = test_app.get('/hello')
    assert response.status_code == 200
    assert response.text == "Hello World!"