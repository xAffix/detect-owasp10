from scanner.xss import scan

def test_xss():
    assert scan("http://testphp.vulnweb.com") == True
