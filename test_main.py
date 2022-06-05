from hello import add

#Set code just to keep CI running
def test_add():
    assert 2 == add(1,1)
