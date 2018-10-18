import packme

def test_always_pass():
    assert True

def test_say_hello_to():
    assert "John" in packme.say_hello_to("John Cleese")
