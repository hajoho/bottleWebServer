# bottleWebServer
proof of concept of a "bottle"-based web server 

# Setup log
1. Set up git repository
1. Set up poetry
    1. ```poetry new bottledemo```
    1. ```poetry shell```
1. Add bottle, pytest and gunicorn (for prod)
    1. ```poetry add bottle pytest WebTest --dev```
    1. ```poetry add bottle gunicorn```
1. Create "bottledemo/app1.py" and "test/test_app1.py"
