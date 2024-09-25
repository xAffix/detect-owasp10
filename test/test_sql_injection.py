from scanner.sql_injection import scan

def test_sql_injection():
    assert scan("http://testphp.vulnweb.com") == True
