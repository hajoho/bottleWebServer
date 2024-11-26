# bottleWebServer
proof of concept of a "bottle"-based web server 

# Setup log
1. Set up git repository
1. Set up poetry
    1. ```poetry new bottleDemo```
    1. ```poetry shell```
1. Add bottle, pytest and gunicorn (for prod)
    1. ```poetry add bottle pytest --dev```
    1. ```poetry add bottle gunicorn```
1. Create "bottledemo/app.py" and "test/test_app.py"
