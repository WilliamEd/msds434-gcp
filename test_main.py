from main import app

#Temp comment till I get file set up how I want
def test_main():
   response = app.test_client().get("/")