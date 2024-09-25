import requests
from .utils import get_all_forms, is_vulnerable
from urllib.parse import urljoin
import time

def scan(url, verbose=False):
    print(f"Scanning {url} for Broken Authentication vulnerabilities...")
    vulnerable = False
    
    forms = get_all_forms(url)
    if verbose:
        print(f"Found {len(forms)} forms.")
    
    for form in forms:
        if is_login_form(form):
            if verbose:
                print(f"Testing form: {form}")
            
            if test_default_credentials(form):
                print("Potential Broken Authentication: Default credentials accepted")
                vulnerable = True
            if test_brute_force(form):
                print("Potential Broken Authentication: No protection against brute force attacks")
                vulnerable = True
            if test_password_complexity(form):
                print("Potential Broken Authentication: Weak password policy")
                vulnerable = True
    
    print("Broken Authentication scan completed.")
    return vulnerable

def is_login_form(form):
    # Improved detection for login forms
    form_str = str(form).lower()
    return ('username' in form_str and 'password' in form_str) or 'login' in form_str

def test_default_credentials(form):
    default_creds = [
        ('admin', 'admin'),
        ('user', 'password'),
        ('root', 'toor')
    ]
    
    for username, password in default_creds:
        response = submit_form(form, {'username': username, 'password': password})
        if response and ('welcome' in response.text.lower() or 'dashboard' in response.text.lower()):
            return True
    return False

def test_brute_force(form):
    for _ in range(10):
        response = submit_form(form, {'username': 'test', 'password': 'wrong'})
        time.sleep(1)
    
    response = submit_form(form, {'username': 'test', 'password': 'wrong'})
    return response and 'login' in response.text.lower()

def test_password_complexity(form):
    response = submit_form(form, {'username': 'newuser', 'password': '123'})
    return response and 'password' not in response.text.lower()

def submit_form(form, data):
    action = form.get('action', '')
    url = urljoin(action, action)
    method = form.get('method', 'post').lower()
    
    try:
        if method == 'post':
            return requests.post(url, data=data, timeout=10)
        return requests.get(url, params=data, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Error submitting form: {e}")
        return None
