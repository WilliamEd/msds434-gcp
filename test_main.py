#from main import app

#Temp comment till I get file set up how I want
#def test_main():
    #response = app.test_client().get("/")

from hello import add

def test_add():
    assert 2 == add(1,1)