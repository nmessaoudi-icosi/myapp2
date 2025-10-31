from app import greet

def test_greet_default():
    assert greet() == "Hello from MyApp2, world!"

def test_greet_custom():
    assert greet("DevOps") == "Hello from MyApp2, DevOps!"
