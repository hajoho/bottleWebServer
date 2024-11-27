from bottledemo import app1
from webtest import TestApp

def test_hello_endpoint():
    test_app = TestApp(app1.app)
    response = test_app.get('/hello')
    assert response.status_code == 200
    assert response.text == "Hello World!"