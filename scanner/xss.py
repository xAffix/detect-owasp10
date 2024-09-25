import requests
from .utils import get_all_forms
from requests.exceptions import RequestException

def scan(url, verbose=False):
    print(f"Scanning {url} for Cross-Site Scripting (XSS) vulnerabilities...")
    
    forms = get_all_forms(url)
    
    for form in forms:
        if test_xss(form, url, verbose):  # Pass url to test_xss
            print(f"Potential XSS vulnerability found in form: {form}")
    
    print("XSS scan completed.")

def test_xss(form, url, verbose=False):
    # XSS payloads to test
    xss_payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "<svg/onload=alert('XSS')>",
        "javascript:alert('XSS')"
    ]
    
    for payload in xss_payloads:
        if verbose:
            print(f"Testing form with payload: {payload}")
        
        # Fill all form inputs with the payload
        data = {input_field: payload for input_field in form.get('inputs', [])}
        response = submit_form(form, data, url)  # Pass url to submit_form
        
        # Check if the payload is reflected in the response
        if response and payload in response.text:
            return True
    
    return False

def submit_form(form, data, method="POST", url=None):
    try:
        action = form.get('action', '')
        if not action:
            action = url  # Default to the current URL if no action is specified
        
        if method == "GET":
            return requests.get(action, params=data)
        return requests.post(action, data=data)
    except RequestException as e:
        print(f"Error submitting form: {e}")
        return None

# This block should be part of your test or the main script, not within the function definitions.
if __name__ == "__main__":
    url = "http://testphp.vulnweb.com"
    forms = get_all_forms(url)  # Fetch forms first

    for form in forms:  # Loop through each form for testing
        response = submit_form(form, {}, method="POST", url=url)  # Adjusting the data to be empty initially

        if response is not None:
            print(f"Response Code: {response.status_code}")  # Print the HTTP response code
            if response.status_code == 200:
                print("Form submitted successfully!")
            else:
                print(f"Form submission failed with response code: {response.status_code}")
        else:
            print("Failed to submit the form.")
