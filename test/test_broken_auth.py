from scanner.broken_auth import scan

def test_broken_auth():
    assert scan("http://testphp.vulnweb.com") == True
